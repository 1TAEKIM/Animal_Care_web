from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    # 기존의 URL 패턴들...
    # path('', views.index, name='index'),
    path('add_dog/', views.add_dog, name='add_dog'),
    # path('submit_dog_info/', views.dog_info_submit, name='dog_info_submit'),
    path('<str:username>/', views.mypage_view, name='mypage_view'),  # username으로 마이페이지 URL 추가
    #path('edit_dog/<int:dog_id>/', views.edit_dog, name='edit_dog'),
    path('dog_edit/<int:pk>/', views.dog_edit, name='dog_edit'),
    path('dog_delete/<int:pk>/', views.dog_delete, name='dog_delete'),

]