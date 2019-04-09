from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.png', upload_to='profile_pics')
    phone = models.CharField(max_length=13)
    county = models.CharField(max_length=20)

    def __str__(self):
        return f"{ self.user.username } Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        max_size = (250,250)

        if img.height > 250 or img.width > 250:
            img.thumbnail(max_size)
            img.save(self.image.path)
