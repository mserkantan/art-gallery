
from django.db import models

import uuid
# Create your models here.

class Museum(models.Model):
    museum_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    place_id = models.ForeignKey("place.Place", on_delete=models.CASCADE)

    museum_name = models.CharField(max_length=50)
    museum_description = models.TextField(blank=True)
    foundation_date = models.DateField()

class MuseumImage(models.Model):
    museum_id = models.ForeignKey("Museum", on_delete=models.CASCADE)
    museum_image = models.ImageField()

