from django.db import models
from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%d/%m/%Y')
    content = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.title} {self.user}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

