from django.db import models
from datetime import datetime

class Performance(models.Model):
	title=models.CharField('Title', default='', max_length=200)
	location=models.CharField('Where', default='', max_length=200)
	date=models.DateField('Date', default=datetime.now())
	meetingTime=models.TimeField('Meeting Time', default=datetime.now())
	startTime=models.TimeField('Start Time', default=datetime.now())
	endTime=models.TimeField('End Time', default=datetime.now())
	details=models.TextField('Details', default='')
