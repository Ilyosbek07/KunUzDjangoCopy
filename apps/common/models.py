from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.post.models import Post


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    device_id = models.CharField(max_length=255)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post'
    )

    def __str__(self):
        return self.device_id

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
