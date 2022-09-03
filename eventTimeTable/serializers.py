from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "event_title",
            "event_time",
            "event_duration",
            "event_speaker",
            "event_location",
        )
