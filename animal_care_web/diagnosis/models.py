from django.db import models

# Create your models here.
class diagnosis(models.Model):
    
    img_url = models.TextField()
    image = models.ImageField(null=True)
    image_name = models.TextField(null=True)
    result = models.CharField(max_length=500, null=True)