from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_diver_grade',
        'default_diver_age',
        'default_country',
    )

    ordering = ('user',)
