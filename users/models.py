from django.db import models
from django.conf import settings


import hashlib
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils import timezone
import pydenticon

# Define a function to generate a default profile picture


def generate_default_profile_pic():
    # Generate an identicon using the user's email address
    email_hash = hashlib.md5('user@example.com'.encode('utf-8')).hexdigest()
    icon = pydenticon.Generator(5, 5).generate(email_hash, 128, 128)
    # Create an in-memory file for the image
    file = io.BytesIO()
    file.write(icon)
    # Create an InMemoryUploadedFile from the in-memory file
    file.seek(0)
    return InMemoryUploadedFile(file, None, 'default.png', '/static/assets/images', file.getbuffer().nbytes, None)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='users/%d/%m/%Y', default=generate_default_profile_pic)

    def __str__(self):
        return f"{self.id} {self.user}"
