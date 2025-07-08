from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.

class Capsule(models.Model):
    STATUS_CHOICES = (
        ('locked', 'Locked'),
        ('unlocked', 'Unlocked'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='capsules')
    title = models.CharField(max_length=255)
    message = RichTextField()
    file = models.FileField(upload_to='capsule_files/', blank=True, null=True)
    recipient_email = models.EmailField()
    unlock_datetime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='locked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_unlocked(self):
        from django.utils import timezone
        return self.status == 'unlocked' or timezone.now() >= self.unlock_datetime

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
