from django.conf import settings
from django.contrib.auth import get_user_model

__all__ = ["User", "AUTH_USER_MODEL"]

AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")

# Get the User model
User = get_user_model()
