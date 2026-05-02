from django.contrib import admin
from .models import TravelImage


@admin.register(TravelImage)
class TravelImageAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")

    def delete_model(self, request, obj):
        if obj.image:
            obj.image.storage.delete(obj.image.name)
        super().delete_model(request, obj)

    def save_model(self, request, obj, form, change):
        if change:
            old = TravelImage.objects.get(pk=obj.pk)
            if old.image and old.image != obj.image:
                old.image.storage.delete(old.image.name)
        super().save_model(request, obj, form, change)
