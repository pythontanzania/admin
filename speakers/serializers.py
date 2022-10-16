from rest_framework import serializers

from .models import Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = (
            "id",
            "name",
            "expertise",
            "topic",
            "email",
            "image",
            "status",
            "profile",
            "website",
        )


class SpeakerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = (
            "name",
            "expertise",
            "topic",
            "email",
            "image",
            "profile",
            "website",
        )
