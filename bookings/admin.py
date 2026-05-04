from django.contrib import admin
from .models import Booking, Traveler, BookingStatusHistory

class TravelerInline(admin.TabularInline):
    model = Traveler
    extra = 0

class BookingHistoryInline(admin.TabularInline):
    model = BookingStatusHistory
    extra = 0
    readonly_fields = ("old_status", "new_status", "created_at")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "schedule",
        "total_amount", "status",
        "created_at"
    )

    list_filter = ("status", "created_at")
    search_fields = (
        "user__username",
        "schedule__tour__title"
    )

    autocomplete_fields = ("user", "schedule")

    inlines = [TravelerInline, BookingHistoryInline]

    list_editable = ("status",)

    date_hierarchy = "created_at"

@admin.register(Traveler)
class TravelerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "booking", "nationality")
    search_fields = ("full_name", "passport_number")