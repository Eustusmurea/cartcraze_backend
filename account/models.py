import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Ensure email is always required

    def __str__(self):
        return f"{self.username} ({self.email})"

class UserProfile(models.Model):
    class GenderOptions(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
        PREFER_NOT_TO_SAY = 'N', _('Prefer not to say')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(max_length=1, choices=GenderOptions.choices, default=GenderOptions.OTHER)
    phone_number = models.CharField(
        max_length=10, 
        blank=True, 
        null=True, 
        validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits.")]
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_gender_display()}"
