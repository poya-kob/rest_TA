from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=30)


class Album(models.Model):
    title = models.CharField(max_length=30)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tracks(models.Model):
    title = models.CharField(max_length=30)
    publish_date = models.DateField(auto_now_add=True)
    singer = models.ManyToManyField(Singer, related_name='track')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, related_name='album_track', null=True)

    def __str__(self):
        return self.title
