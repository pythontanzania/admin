from rest_framework import generics, permissions

from django.shortcuts import render

from .models import Speaker
from .serializers import SpeakerSerializer, SpeakerCreateSerializer


# Everyone should access
class SpeakersList(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


# Everyone can create
class SpeakersCreate(generics.CreateAPIView):
    serializer_class = SpeakerCreateSerializer


# Only Admin can edit and delete
class SpeakersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
