from django.db import models
from phone_field import PhoneField

# Create your models here.

class Speaker(models.Model):
    speaker_name = models.CharField(max_length=200)
    speaker_field = models.CharField(max_length=500)  # speaker career/expertise
    speaker_topic = models.CharField(max_length=500)
    speaker_email = models.EmailField()
    speaker_phone = PhoneField(blank=True, help_text="Contact phone number")

    def __str__(self):
        return self.speaker_name
