from django.db import models
from mezzanine.pages.models import Page

# Create your models here.
class ApplyLink(Page):
    url = models.URLField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    permit = models.BooleanField()

