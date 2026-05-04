from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, UserProfile, Agent


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("-date_joined",)

    list_display = (
        "email",
        "phone",
        "full_name",
        "role",
        "is_active",
        "is_staff",
        "is_verified",
        "date_joined",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
        "is_verified",
    )

    search_fields = ("email", "phone", "first_name", "last_name")

    readonly_fields = ("id", "date_joined", "last_login")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name", "phone")}),
        (_("Roles & Permissions"), {
            "fields": (
                "role",
                "is_active",
                "is_staff",
                "is_superuser",
                "is_verified",
                "groups",
                "user_permissions",
            )
        }),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "phone",
                "first_name",
                "last_name",
                "password1",
                "password2",
                "role",
                "is_staff",
                "is_active",
            ),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")

    autocomplete_fields = ()

    inlines = [UserProfileInline]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "nationality")
    search_fields = ("user__email", "passport_number")

    autocomplete_fields = ("user",)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ("user", "company_name", "license_number", "is_approved")
    list_filter = ("is_approved",)

    search_fields = ("company_name", "user__email")

    autocomplete_fields = ("user",)

    list_editable = ("is_approved",)
