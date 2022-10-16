from django.db import models

# Create your models here.


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    expertise = models.CharField(max_length=500)
    topic = models.CharField(max_length=500)
    email = models.EmailField()
    image = models.ImageField('images', blank=True, null=True)
    status = models.CharField(max_length=100, default="Pending", blank=True)
    profile = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
