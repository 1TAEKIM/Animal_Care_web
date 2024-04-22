from django.db import models
from accounts.models import CustomUser
from django.conf import settings
# from accounts.models import Users

class Categories(models.Model):
    category = models.CharField(max_length=100)


# Create your models here.
class Products(models.Model):
    
    detail_category = models.ManyToManyField(Categories)
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, null=True)
    content = models.TextField()
    price = models.IntegerField()
    
    # 어떻게 할지 아직 몰라서
    img_url = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products_user_info')
    # user_grade = models.ForeignKey(Users, on_delete=models.CASCADE)
    

