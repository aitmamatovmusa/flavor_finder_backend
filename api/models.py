from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    address = models.CharField(max_length=255)
    num_reviews = models.IntegerField()
    average_price = models.IntegerField()
    map_link = models.CharField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    rating = models.FloatField()
    review = models.TextField()
    place_id = models.ForeignKey(
        Place, related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user_name
