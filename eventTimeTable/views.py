from rest_framework import generics, permissions

from django.shortcuts import render

from .models import Event
from .serializers import EventSerializer

# Everybody can access
class EventsList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Only Admin can access
class EventCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = EventSerializer


# Only Admin can access
class EventsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
