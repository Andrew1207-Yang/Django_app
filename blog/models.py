from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=False, default="Andrew")
    article_type = models.CharField(max_length=100, unique=False, default="Blog")
    preview = models.TextField(blank=True,null=True, default = "No Preview Availible")
    preview_image = models.ImageField(upload_to = '.',default = "default.jpg", null = True, blank = True)
    # content = RichTextField(blank=True,null=True)
    # content = models.TextField(blank = True, Null = True)
    content = RichTextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("blog:detail_view",kwargs = {"pk":self.id,"title": self.title})


