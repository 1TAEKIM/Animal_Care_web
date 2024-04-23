














from django.urls import path
from . import views


app_name = 'mypage'
urlpatterns = [
    # 기존의 URL 패턴들...
    # path('', views.index, name='index'), 
    path('add_dog/<str:username>/', views.add_dog, name='add_dog'),
    path('submit_dog_info/<str:username>/', views.dog_info_submit, name='dog_info_submit'),
    path('<str:username>/', views.mypage_view, name='mypage_view'),  # username으로 마이페이지 URL 추가
]