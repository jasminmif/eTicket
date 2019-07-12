from django.db import models


# Create your models here.
class Ticket(models.Model):
    uuid_code = models.CharField(max_length=200, null=True, blank=True, unique=True)
    used = models.BooleanField(default=False)
    printed = models.BooleanField(default=False)