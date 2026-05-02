from django.db import models
from config.models import TimeStampedModel
from bookings.models import Booking


class Payment(TimeStampedModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    )

    METHOD_CHOICES = (
        ("stripe", "Stripe"),
        ("sslcommerz", "SSLCommerz"),
        ("manual", "Manual"),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10)

    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    paid_at = models.DateTimeField(null=True, blank=True)
