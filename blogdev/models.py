from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django_quill.fields import QuillField
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    tags = TaggableManager()
    cover_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title
