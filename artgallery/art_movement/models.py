import uuid

from django.db import models

# Create your models here.
class Art_Movement(models.Model):
    movement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movement_name = models.CharField(max_length=40)
    movement_description = models.TextField()
    movement_era = models.CharField(max_length=100, null=True)
    movement_picture = models.ImageField(blank=True, null=True)

    
