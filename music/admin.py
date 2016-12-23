from django.contrib import admin
from .models import Album

# tell django that the album table needs an admin interface

admin.site.register(Album)

