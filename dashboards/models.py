from django.db import models
from django.shortcuts import render, get_object_or_404
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User



STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)
class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    blog_body = CKEditor5Field('blog body', config_name='extends') 
    auther = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default = "Draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
