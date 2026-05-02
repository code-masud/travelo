from django.conf import settings
from django.db import models
from config.models import TimeStampedModel
from tours.models import TourSchedule


User = settings.AUTH_USER_MODEL


class Booking(TimeStampedModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    schedule = models.ForeignKey(TourSchedule, on_delete=models.PROTECT)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.user} - {self.schedule}"


class Traveler(TimeStampedModel):
    booking = models.ForeignKey(
        Booking, related_name="travelers", on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    passport_number = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class BookingStatusHistory(TimeStampedModel):
    booking = models.ForeignKey(
        Booking, related_name="history", on_delete=models.CASCADE)

    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
