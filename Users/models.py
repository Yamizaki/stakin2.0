from django.contrib.auth.models import User
from django.db import models
class Profile(models.Model):
    # Relación uno a uno con el modelo User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos adicionales que quieras agregar
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'