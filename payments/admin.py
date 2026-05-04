from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "booking", "amount", "currency",
        "method", "status", "paid_at"
    )

    list_filter = ("status", "method")
    search_fields = ("transaction_id", "booking__id")

    autocomplete_fields = ("booking",)

    readonly_fields = ("transaction_id", "paid_at")

    date_hierarchy = "created_at"