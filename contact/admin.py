from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'ticket_number',
        'first_name',
        'email',
    )

    ordering = ('ticket_number',)
