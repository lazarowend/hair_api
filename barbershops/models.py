from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class Barbershop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    phone = models.CharField(11)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=255)
    image_profile = models.ImageField(upload_to='media/profile/', blank=True, null=True)
    
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name