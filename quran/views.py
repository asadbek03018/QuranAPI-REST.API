from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SuraSerializer, OyatForSuraSerializer, SuraForOyatSerializer, SuraForView

from .models import Sura, Oyat, Author


# Create your views here.

# class SuraList(generics.RetrieveAPIView):
#     queryset = Sura.objects.all()
#     serializer_class = SuraSerializer

# class SuraList(APIView):
#     def get(self, request, sura_name):
#         sura = Sura.objects.get(name=sura_name)
#
#
#         serializer = SuraSerializer(sura)
#         # print(serializer.data)
#         return Response(serializer.data)

# class SuraList(generics.RetrieveAPIView):

#     serializer_class = SuraSerializer

#     #Quronni /api/v2/uz/quran/1/ bu quronning birinchi surasini ko'rsatib beradi
#     def get_queryset(self, *args, **kwargs):

#         return Sura.objects.filter(id=self.kwargs['pk'])



# class SuraDetail(generics.RetrieveAPIView):
#     serializer_class = OyatForSuraSerializer

#     def get_object(self):
#         sura_id = self.kwargs['pk']
#         oyat_number = self.kwargs['oyat_number']

#         sura = get_object_or_404(Sura, pk=sura_id)
#         oyat = sura.oyat.get(oyat_number=oyat_number)
#         return oyat


def home(request):
    return render(request, 'index.html')


def all_suras(request):
    suras = Sura.objects.all().values('id', 'name')
    serializer = SuraForView(suras, many=True)
    return JsonResponse(serializer.data, safe=False)

class SuraList(generics.RetrieveAPIView):
    serializer_class = SuraSerializer

    def get_queryset(self):
        # Filter by language and ID
        lang = self.kwargs.get('lang')
        sura_id = self.kwargs.get('id')
        return Sura.objects.filter(lang=lang, id=sura_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise Http404("Sura mavjud emas!")
        return obj
    
        

class SuraDetail(generics.RetrieveAPIView):
    serializer_class = OyatForSuraSerializer

    def get_object(self):
        # Retrieve keyword arguments from the URL
        lang = self.kwargs['lang']
        sura_id = self.kwargs['id']
        oyat_number = self.kwargs['oyat_number']
        
        # Get the specific Sura object based on lang and id
        sura = get_object_or_404(Sura, lang=lang, id=sura_id)
        
        # Retrieve the specific Oyat (verse) from the related Oyat set using 'oyatlar'
        oyat = get_object_or_404(sura.oyatlar, oyat_number=oyat_number)
        
        return oyat












