from django.urls import path
from .views import SuraList, SuraDetail, all_suras
app_name = 'quran_uz'
urlpatterns = [
    path('quran/suras/', all_suras, name='suras'),
    path('quran/<str:lang>/<int:id>/', SuraList.as_view(), name='sura-list-uz'),
    path('quran/<str:lang>/<int:id>/<int:oyat_number>/', SuraDetail.as_view(), name='oyat-detail-uz')
]