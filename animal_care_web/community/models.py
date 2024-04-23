from django.db import models
from django.conf import settings


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)  # 사용자 없어도 글은 남아있음. 맞냐
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    hits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title




