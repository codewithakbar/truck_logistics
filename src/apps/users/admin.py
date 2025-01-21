from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django.utils.html import format_html


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "get_full_name",
        "email",
        "user_type",
        "is_staff",
        "is_active",
        "last_login",
    )
    list_filter = ("user_type", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    'email',
                    "father_name",
                    "birthday_date",
                    "gender",
                    "phone_number",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("User Type", {"fields": ("user_type",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    ordering = ("username",)
    search_fields = ("username", "first_name", "last_name", "email")
    filter_horizontal = ("groups", "user_permissions")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    get_full_name.short_description = "Full name"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "display_avatar")

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="50" height="50" />', obj.avatar.url
            )
        return "No Avatar"

    display_avatar.short_description = "Avatar"


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
