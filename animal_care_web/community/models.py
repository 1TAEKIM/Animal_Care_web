from django.db import models


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey()
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)




