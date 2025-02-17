import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.EmailField(_('email address'), unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
      return f"{self.username}"
  
class UserProfile(models.Model):
   class GenderOptions(models.TextChoices):
        MALE = 'M', _('male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
        PREFER_NOT_TO_SAY = 'N', _('Prefer not to say')

user = models.OneToOneField(User, on_delete=models.CASCADE)
first_name = models.CharField(max_length=100)
last_name = models.CharField(max_length=100)
gender = models.CharField(max_length=1, choices=UserProfile.GenderOptions.choices, default=UserProfile.GenderOptions.OTHER)
phone_number = models.CharField(max_length=10, blank=True, null=True)
date_joined = models.DateTimeField(auto_now_add=True)
last_login = models.DateTimeField(auto_now=True)
last_updated = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.user.username}"
   