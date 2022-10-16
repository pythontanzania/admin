from rest_framework import serializers

from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = (
            "id",
            "name",
            "image",
        )
