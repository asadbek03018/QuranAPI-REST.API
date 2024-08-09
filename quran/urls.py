from django.urls import path
from .views import SuraList, SuraDetail
app_name = 'quran_uz'
urlpatterns = [
    path('quran/<str:lang>/<int:id>/', SuraList.as_view(), name='sura-list-uz'),
    path('quran/<str:lang>/<int:id>/<int:oyat_number>/', SuraDetail.as_view(), name='oyat-detail-uz')
]