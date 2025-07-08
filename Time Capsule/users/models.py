from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # Add extra fields here if needed (e.g., profile pic, stats)
    pass
