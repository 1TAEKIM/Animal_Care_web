"""
URL configuration for animal_care_web project.

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
from . import views
from django.conf.urls.static import static
from animal_care_web import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('disease_information/', views.disease_information, name='disease_information'),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('mypage/', include('mypage.urls')),
    path('products/', include('products.urls')),
    path('diagnosis/', include('diagnosis.urls')),
    
    

]

# image URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
