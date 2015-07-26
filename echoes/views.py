from django.shortcuts import render

from .models import Performance

def performances(request):
	performances = Performance.objects.all()
	fields=Performance._meta.get_fields()
	context = {'performances': performances, 'fields':fields }
	return render(request, 'echoes/performances.html', context)

def homepage(request):
	return render(request, 'echoes/homepage.html')
