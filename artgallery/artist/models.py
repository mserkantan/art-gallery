import uuid

from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist_name = models.CharField(max_length=40)
    artist_surname = models.CharField(max_length=40)
    artist_birthdate = models.DateField(default="-")
    artist_deathdate = models.DateField(default="-")
    place_born = models.ForeignKey("place.Place", on_delete=models.CASCADE, related_name="place_born", default="1")
    place_death = models.ForeignKey("place.Place", on_delete=models.CASCADE, related_name="place_death", default="1")


class Artist_Image(models.Model):
    of_artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

class OfArtist(models.Model):
    art_movement = models.ForeignKey("art_movement.Art_Movement", on_delete=models.CASCADE, blank=True, null=True)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, blank=True, null=True)


