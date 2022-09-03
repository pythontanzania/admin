from django.db import models

# Create your models here.


class Speaker(models.Model):
    speaker_name = models.CharField(max_length=200)
    speaker_expertise = models.CharField(max_length=500)
    speaker_topic = models.CharField(max_length=500)
    speaker_email = models.EmailField()
    speaker_status = models.CharField(max_length=100, default="Pending", blank=True)

    def __str__(self):
        return self.speaker_name
