from django.db import models
from django.conf import settings

class Categories(models.Model):
    category = models.CharField(max_length=100)

    def __srt__(self):
        return self.name

# Create your models here.
class Products(models.Model):
    
    detail_category = models.ManyToManyField(Categories)
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, null=True)
    content = models.TextField()
    price = models.IntegerField()
    
    img_url = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    

    def __srt__(self):
        return self.name