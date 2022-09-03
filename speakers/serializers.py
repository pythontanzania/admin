from rest_framework import serializers

from .models import Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = (
            "id",
            "speaker_name",
            "speaker_expertise",
            "speaker_topic",
            "speaker_email",
            "speaker_status",
        )


class SpeakerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = (
            "speaker_name",
            "speaker_expertise",
            "speaker_topic",
            "speaker_email",
        )
