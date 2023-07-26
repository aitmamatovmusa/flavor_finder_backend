from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    num_reviews = models.IntegerField()
    average_price = models.IntegerField()
    map_link = models.CharField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    rating = models.FloatField()
    review = models.TextField()
    place = models.ForeignKey(
        Place,
        related_name="comments",
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

        place_comments = self.place.comments
        num_reviews = place_comments.count()

        if num_reviews > 0:
            average_rating = place_comments.aggregate(models.Avg("rating"))[
                "rating__avg"
            ]
            self.place.num_reviews = num_reviews
            self.place.rating = average_rating
            self.place.save()

    def __str__(self):
        return self.user_name
