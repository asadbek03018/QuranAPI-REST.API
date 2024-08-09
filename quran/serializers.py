from rest_framework import serializers
from .models import Sura, Author, Oyat


class AuthorForOyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('full_name', 'image', 'age', 'about')

class OyatForSuraSerializer(serializers.ModelSerializer):
    author = AuthorForOyatSerializer()

    class Meta:
        model = Oyat
        fields = ('oyat_number', 'translate', 'audio', 'author')




# class OyatForSuraSerializer(serializers.ModelSerializer):
#     author = AuthorForOyatSerializer()
#     class Meta:
#         audio = Oyat.audio
#         model = Oyat
#         ref_name = 'OyatUzbek'
#         fields = ('oyat_number', 'translate', 'audio', 'author')


class SuraSerializer(serializers.ModelSerializer):
    oyatlar = OyatForSuraSerializer(many=True)  # Use the correct related name 'oyatlar'

    class Meta:
        model = Sura
        ref_name = 'SuraUzbek'
        fields = ('name', 'total_oyat', 'oyatlar', 'written_place')  # Update fields to include 'oyatlar'
        

class SuraForOyatSerializer(serializers.ModelSerializer):
    oyatlar = OyatForSuraSerializer(many=True)

    class Meta:
        model = Sura
        ref_name = 'SuraForOyatUzbek'
        fields = ('name', 'total_oyat', 'oyatlar', 'written_place')


