from django.db import models


class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_time = models.DateTimeField()
    event_duration = models.DurationField()
    event_speaker = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)

    def __str__(self):
        return self.event_title
