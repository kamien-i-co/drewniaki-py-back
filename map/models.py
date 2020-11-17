from django.db import models

class Marker(models.Model):
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
    photos = models.CharField(blank=True, max_length=1024) # models.ArrayField(models.TextField(blank=True), size=64) postgres only
    coords = models.CharField(blank=True, max_length=32) # models.ArrayField(models.FloatField(blank=True), size=2) -- ,, --