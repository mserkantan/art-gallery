
from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=20)
    user_real_name = models.CharField(max_length=30, null=True)
    user_surname = models.CharField(max_length=30, null=True)
    user_picture = models.ImageField(blank=True, null=True)
    user_birthdate = models.DateField(null=True)

class Contact(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_email = models.EmailField()
    user_phone_number = models.CharField(max_length=15, null=True)

class FavouriteArtMovement(models.Model):
    fav_art_movement = models.ForeignKey("art_movement.Art_Movement", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, blank=True, null=True)

class FavouriteArtist(models.Model):
    fav_artist = models.ForeignKey("artist.Artist", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, blank=True, null=True)

class FavouriteArtObject(models.Model):
    fav_art_object = models.ForeignKey("art_object.Artifact", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, blank=True, null=True)

class FavouriteMuseum(models.Model):
    fav_museum = models.ForeignKey("museum.Museum", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, blank=True, null=True)