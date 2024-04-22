from django.db import models
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
    img_url = models.URLField(null=True)
    img_dir = models.ImageField(upload_to='product_images/', null=True)
    
    # user_grade = models.ForeignKey(Users, on_delete=models.CASCADE)
    

