from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField()
    duration = models.DurationField()
    speaker = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
