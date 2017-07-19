from __future__ import unicode_literals

from django.db import models

class Room(models.Model):
	temp=models.FloatField()
	humi=models.FloatField()
