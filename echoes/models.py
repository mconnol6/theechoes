from django.db import models
from django.utils import timezone

class Performance(models.Model):
	title=models.CharField('Title', default='', max_length=200)
	location=models.CharField('Where', default='', max_length=200)
	date=models.DateField('Date', default=timezone.now)
	meetingTime=models.TimeField('Meeting Time', default=timezone.now)
	startTime=models.TimeField('Start Time', default=timezone.now)
	endTime=models.TimeField('End Time', default=timezone.now)
	details=models.TextField('Details', default='')
