from django.contrib import admin
from .models import Capsule

@admin.register(Capsule)
class CapsuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'recipient_email', 'unlock_datetime', 'status')
    list_filter = ('status', 'unlock_datetime')
    search_fields = ('title', 'recipient_email', 'user__username')
