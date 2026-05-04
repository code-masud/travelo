import uuid
from django.db import models


class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Agency(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    website = models.URLField(blank=True)

    logo = models.ImageField(upload_to="agencies/", blank=True)

    description = models.TextField(blank=True)

    address = models.TextField()

    country = models.ForeignKey(
        "locations.Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
