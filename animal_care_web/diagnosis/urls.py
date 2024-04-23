from django.urls import path
from . import views

app_name = 'diagnosis'

urlpatterns = [
    path('', views.index, name='index'),
    path('img_detail/<int:pk>/', views.img_detail, name='img_detail'),
    path('s3_image_download/<int:image_key>/', views.S3ImageDownloadView, name='s3_image_download'),
]