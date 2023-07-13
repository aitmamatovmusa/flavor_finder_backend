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