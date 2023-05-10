from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='users/%d/%m/%Y', blank=True)


    def __str__(self):
        return f"{self.id} {self.user}"