from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    # ... 기존의 url 패턴들 ...
    path('', views.index, name='index'),
    path('add_dog/', views.add_dog, name='add_dog'),
    path('submit_dog_info/', views.dog_info_submit, name='dog_info_submit'),
]

