
import uuid

from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Place(models.Model):
    place_country = models.CharField(max_length=50)
    place_city = models.CharField(max_length=50)
    place_zip = models.IntegerField( validators=[MaxValueValidator(99999)])
    place_description = models.TextField()


