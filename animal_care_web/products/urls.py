from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('management/', views.management, name='management'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete')
    
]