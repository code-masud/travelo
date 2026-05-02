from django.db import models
from config.models import TimeStampedModel
from locations.models import Country, City


class TourCategory(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tour(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    description = models.TextField()
    duration_days = models.PositiveIntegerField()

    category = models.ForeignKey(
        TourCategory, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default="USD")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Itinerary(TimeStampedModel):
    tour = models.ForeignKey(
        Tour, related_name="itinerary", on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()

    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["day_number"]


class Inclusion(TimeStampedModel):
    tour = models.ForeignKey(
        Tour, related_name="inclusions", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class Exclusion(TimeStampedModel):
    tour = models.ForeignKey(
        Tour, related_name="exclusions", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class TourImage(TimeStampedModel):
    tour = models.ForeignKey(
        Tour, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tours/")
    is_primary = models.BooleanField(default=False)


class TourSchedule(TimeStampedModel):
    tour = models.ForeignKey(
        Tour, related_name="schedules", on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField()

    total_slots = models.PositiveIntegerField()
    booked_slots = models.PositiveIntegerField(default=0)

    price = models.DecimalField(max_digits=12, decimal_places=2)

    is_active = models.BooleanField(default=True)

    def available_slots(self):
        return self.total_slots - self.booked_slots


class Coupon(TimeStampedModel):
    code = models.CharField(max_length=50, unique=True)

    discount_percent = models.PositiveIntegerField(null=True, blank=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    is_active = models.BooleanField(default=True)


class CancellationPolicy(TimeStampedModel):
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE)

    refund_percentage = models.PositiveIntegerField()
    days_before = models.PositiveIntegerField()
