from rest_framework import serializers

from .models import Place, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user_name", "rating", "review", "place")


class PlaceSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "rating",
            "address",
            "num_reviews",
            "average_price",
            "map_link",
            "comments",
        )
