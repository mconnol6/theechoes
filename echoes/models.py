from django.db import models

class Performance(models.Model):
	title=models.CharField(max_length=200)
