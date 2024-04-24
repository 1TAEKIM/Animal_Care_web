from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    path('board/<int:pk>/', views.posting, name='posting'),
    path('board/postwrite/', views.postwrite, name='postwrite'),
    path('board/<int:pk>/delete/', views.delete, name='delete'),
    path('board/<int:pk>/postupdate/', views.postupdate, name='postupdate'),
    path('board/<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('board/<int:post_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('board/<int:pk>/like/', views.post_like, name='post_like'),

]