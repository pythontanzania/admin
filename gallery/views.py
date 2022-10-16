from rest_framework import generics, permissions

from django.shortcuts import render

from .models import Gallery
from .serializers import GallerySerializer


# Everyone should access
class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


# Admin can create
class GalleryCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = GallerySerializer


# Only Admin can edit and delete
class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

