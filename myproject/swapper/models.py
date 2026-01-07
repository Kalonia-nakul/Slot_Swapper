from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


class Slots(models.Model): 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    topic = models.CharField(max_length=150)
    Date = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    status = models.CharField(max_length=20, choices=[('swappable', 'Swappable'), ('busy', 'Busy'), ('not_swappable', 'Not Swappable')])
    request_swap = models.BooleanField(default=False)
    swap_with = models.IntegerField(null=True, blank=True)  # Assuming this is the ID of aother slot