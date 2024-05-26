from django.db import models
from django.contrib.auth.models import User

class Barbershop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    phone = models.CharField(11)
    image_profile = models.ImageField(upload_to='media/profile/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')

    def __str__(self):
        return self.name