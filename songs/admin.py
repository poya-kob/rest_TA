from django.contrib import admin

from .models import Singer, Tracks, Album

admin.site.register(Singer)
admin.site.register(Tracks)
admin.site.register(Album)
