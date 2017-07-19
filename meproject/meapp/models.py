from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AtmosLog(models.Model):
	timestamp=models.DateTimeField(auto_now_add=True)
	temp=models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=1)
	humi=models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=1)

