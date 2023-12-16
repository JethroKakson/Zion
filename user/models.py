from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shin_id = models.CharField(max_length=20, default='SCJ00000000')
    duty = models.CharField(max_length=20, default='신쳔지')
    contact = models.CharField(max_length=15, default='+25600000000')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user}\'s profile'

