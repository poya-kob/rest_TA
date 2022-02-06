import http

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from .serializers import SingerSerializer, TrackSerializer, TrackDetailSerializer
from .models import Singer, Tracks
from .filters import TracksFilterSet


class CustomPage(PageNumberPagination):
    page_size = 1


# class SingersView(APIView):
#     def get(self, request):
#         singers = Singer.objects.all()
#         serialized = SingerSerializer(singers, many=True)
#         return Response(serialized.data)
#
#     def post(self, request):
#         serialized = SingerSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response({'error': 'not valid data'})

class SingersView(ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingersDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class TrackView(ListCreateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TrackSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['title', 'singer__name']
    filterset_class = TracksFilterSet
    search_fields = ['title', 'singer__name']
    pagination_class = CursorPagination
    # def get_queryset(self):
    #     q = Tracks.objects.all()
    #     title = self.request.query_params.get('title')
    #     q = q.filter(title=title)
    #     return q


class TrackDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TrackDetailSerializer
    queryset = Tracks.objects.all()
