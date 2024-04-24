from django.db import models

# Create your models here.

from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# 강아지 모델
class Dog(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 소유자
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 소유자
    name = models.CharField(max_length=100)  # 이름
    breed = models.CharField(max_length=100)  # 종
    age = models.PositiveIntegerField()  # 나이
    image = models.ImageField(upload_to='dog_images/', default='default_image.jpg')

    
