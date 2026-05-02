from django.db import models
from travel.storage import SupabaseStorage

supabase_storage = SupabaseStorage()

class TravelImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(storage=supabase_storage)
    uploaded_at = models.DateTimeField(auto_now_add=True)