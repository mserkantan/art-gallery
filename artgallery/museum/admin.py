from django.contrib import admin

# Register your models here.
from .models import Museum, MuseumImage

admin.site.register(Museum)
admin.site.register(MuseumImage)