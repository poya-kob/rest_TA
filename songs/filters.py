from django_filters.rest_framework import FilterSet
from .models import Tracks


class TracksFilterSet(FilterSet):
    class Meta:
        model = Tracks
        fields = {
            'title': ['icontains']
        }
