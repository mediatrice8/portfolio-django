from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=50, unique=True)
    
    # def __str__(self):
    #     return self.location_name

