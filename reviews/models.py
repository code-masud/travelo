from django.conf import settings
from django.db import models
from config.models import TimeStampedModel
from tours.models import Tour


User = settings.AUTH_USER_MODEL


class Review(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(
        Tour, related_name="reviews", on_delete=models.CASCADE)

    rating = models.PositiveIntegerField()
    comment = models.TextField()
