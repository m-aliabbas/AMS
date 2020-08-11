from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
from datetime import timedelta


def get_expiry():
    return datetime.now() + timedelta(days=30)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_type = models.BooleanField(default=0)
    creation_date = models.DateTimeField(default=datetime.now)
    expire_date = models.DateTimeField(default=get_expiry)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2,default=50.00)
    payment_status = models.BooleanField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} Payment'