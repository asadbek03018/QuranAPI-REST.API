"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from quran.views import home
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Quran Online API",
      default_version='v3.0',
      description="Bu api orqali siz quronu karimning oyatlari suralari va ma'nolarini topishingiz mumkin. Audiolari bilan birga",
      terms_of_service="https://t.me/asadbek_074/",
      contact=openapi.Contact(email="asadbekoffical1202@gmail.com"),

   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)





urlpatterns = [
    path('', home, name='home'),
    path('api/v3/admin/', admin.site.urls),
    path('api/auth/login/uz/', include('rest_framework.urls')),
    path('api/v3/', include('quran.urls')), #Lang uz
    







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


