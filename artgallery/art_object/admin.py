from django.contrib import admin

# Register your models here.
from .models import Artifact, ArtifactImage, Painting, Sculpture, Photograph, OfObject

admin.site.register(ArtifactImage)
admin.site.register(OfObject)
admin.site.register(Painting)
admin.site.register(Sculpture)
admin.site.register(Photograph)
