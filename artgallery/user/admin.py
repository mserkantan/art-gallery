from django.contrib import admin

# Register your models here.
from .models import User, Contact, FavouriteArtMovement, FavouriteArtist, FavouriteArtObject, FavouriteMuseum

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(FavouriteArtMovement)
admin.site.register(FavouriteArtist)
admin.site.register(FavouriteArtObject)
admin.site.register(FavouriteMuseum)