from django.db import models

# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    file = models.CharField(max_length=500)

    def __str__(self):
        return self.title
