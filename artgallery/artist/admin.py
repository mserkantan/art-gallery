from django.contrib import admin
from django.apps import apps

# Register your models here.
from .models import Artist, Artist_Image, OfArtist



admin.site.register(Artist)
admin.site.register(OfArtist)
admin.site.register(Artist_Image)
#admin.site.register(apps.get_model('art_object'),)