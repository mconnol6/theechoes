from django.db import models
from django.utils import timezone

class Performance(models.Model):
	def __str__(self):
		return self.title
	title=models.CharField('Title', default='', max_length=200)
	location=models.CharField('Where', default='', max_length=200)
	date=models.DateField('Date', default='')
	meetingTime=models.TimeField('Meeting Time', default='')
	startTime=models.TimeField('Start Time', default='')
	endTime=models.TimeField('End Time', default='')
	details=models.TextField('Details', default='')
