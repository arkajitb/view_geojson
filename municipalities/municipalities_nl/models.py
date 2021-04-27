from django.contrib.gis.db import models

# Location table to store all the feature objects.
class Location(models.Model):
	geometry  = models.MultiPolygonField()
	name = models.CharField(max_length = 255, null = False, unique = True)
