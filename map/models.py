from django.db import models
from django.contrib.postgres.fields import ArrayField

class Marker(models.Model):
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
    monument = models.ForeignKey('Monument', related_name="markers", on_delete=models.CASCADE)

class Photo(models.Model):
    name = models.TextField(blank=True)
    url = models.TextField(blank=True)
    # models.ImageField(upload_to=directory)
    monument = models.ForeignKey('Monument', related_name="photos", on_delete=models.CASCADE)

class Monument(models.Model):
    CHOICES = (
        ('0', 'Historical'),
        ('1', 'Very Good'),
        ('2', 'Good'),
        ('3', 'Moderate'),
        ('4', 'Bad'),
        ('5', 'Very Bad'),
        ('6', 'Destroyed'),
        ('7', 'Unknown'),
    )
    name = models.TextField(blank=True)
    state= models.CharField(blank=True, max_length=32, choices=CHOICES)
    description = models.TextField(blank=True)
