from django.contrib import admin
from .models import (
    TourCategory, Tour, Itinerary, Coupon, CancellationPolicy,
    Inclusion, Exclusion, TourImage, TourSchedule
)


class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 1


class InclusionInline(admin.TabularInline):
    model = Inclusion
    extra = 1


class ExclusionInline(admin.TabularInline):
    model = Exclusion
    extra = 1


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        "title", "country", "city",
        "base_price", "currency",
        "is_active", "created_at"
    )

    list_filter = ("is_active", "country", "city", "category")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}

    autocomplete_fields = ("country", "city", "category")

    inlines = [
        ItineraryInline,
        InclusionInline,
        ExclusionInline,
        TourImageInline,
    ]

    list_editable = ("is_active",)

    date_hierarchy = "created_at"


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(TourSchedule)
class TourScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "tour", "start_date", "end_date",
        "total_slots", "booked_slots",
        "price", "is_active"
    )

    list_filter = ("is_active", "start_date")
    search_fields = ("tour__title",)

    autocomplete_fields = ("tour",)

    date_hierarchy = "start_date"


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "discount_percent",
                    "valid_from", "valid_to", "is_active")
    list_filter = ("is_active",)
    search_fields = ("code",)


@admin.register(CancellationPolicy)
class CancellationPolicyAdmin(admin.ModelAdmin):
    list_display = ("tour", "refund_percentage", "days_before")
    autocomplete_fields = ("tour",)
