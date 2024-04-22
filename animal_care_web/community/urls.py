from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('/', views.index, name='index'),
    path('/board/', views.board, name='board'),
    path('/board/<int:pk>/', views.posting, name='posting'),
    path('/board/postwrite/', views.postwrite, name='postwrite'),
    path('/board/<int:pk>/delete/', views.delete, name='delete'),
    path('/board/<int:pk>/postupdate/', views.postupdate, name='postupdate'),
]