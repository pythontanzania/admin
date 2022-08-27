from django.db import models
from phone_field import PhoneField

# Create your models here.


class Speakers(models.Model):
    name = models.CharField(max_length=200)
    field = models.CharField(max_length=500)
    topic = models.CharField(max_length=500)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text="Contact phone number")
