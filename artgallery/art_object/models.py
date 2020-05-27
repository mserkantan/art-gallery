import uuid

from django.db import models


# Create your models here.
class Artifact(models.Model):
    artist_id = models.ForeignKey("artist.Artist", on_delete=models.CASCADE, default=uuid.uuid4)
    museum_id = models.ForeignKey("museum.Museum", on_delete=models.CASCADE, default=uuid.uuid4)
    artifact_title = models.CharField(max_length=50)
    artifact_original_title = models.CharField(max_length=50)
    artifact_description = models.TextField()
    artifact_creation = models.DateField()

class ArtifactImage(models.Model):
    artifact_id = models.ForeignKey("Artifact", on_delete=models.CASCADE)
    artifact_image = models.ImageField()

class OfObject(models.Model):
    artifact = models.ForeignKey("Artifact", on_delete=models.CASCADE, blank=True, null=True)
    art_movement = models.ForeignKey("art_movement.Art_Movement", on_delete=models.CASCADE, blank=True, null=True)

class Painting(Artifact):
    type = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    width =  models.FloatField(blank=True)
    height =  models.FloatField(blank=True)

class Sculpture(Artifact):
    material = models.CharField(max_length=30)
    height =  models.FloatField(blank=True)
    weight =  models.FloatField(blank=True)

class Photograph(Artifact):
    place = models.CharField(max_length=30)
    width =  models.FloatField(blank=True)
    height =  models.FloatField(blank=True)
