from django.contrib import admin
from .models import Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "created_at")
    search_fields = ("name", "code")
    ordering = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "created_at")
    list_filter = ("country",)
    search_fields = ("name",)
    autocomplete_fields = ("country",)