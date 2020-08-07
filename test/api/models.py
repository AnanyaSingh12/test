from django.db import models
from .constants import *


# Create your models here.
DEVICE_TYPE = [
    (ANDROID, 'Android'),
    (IOS, 'ios'),
]

class Device(models.Model):
    platform = models.CharField(max_length=50,choices=DEVICE_TYPE, null=True, blank=True)
    version = models.FloatField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_device'