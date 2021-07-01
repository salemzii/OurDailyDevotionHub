from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_photo = models.ImageField(default = 'default.jpg', blank=True, upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length = 120)

    
    def __str__(self):
        template = f"{self.user.username}'s profile."
        return template.format(self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

