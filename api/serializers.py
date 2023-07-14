from django.db.models import fields
from rest_framework import serializers

from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Place
        fields = (
            "name",
            "rating",
            "address",
            "num_reviews",
            "average_price",
            "map_link",
        )
