from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string
from django_cryptography.fields import encrypt
from uuid import UUID
from fernet_fields import EncryptedTextField

# Create your models here.
from wagtail.core.models import Page






