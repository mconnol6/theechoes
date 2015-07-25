from django.shortcuts import render

from .models import Performance

def performances(request):
	performances = Performance.objects.all()
	context = {'performances': performances }
	return render(request, 'echoes/performances.html', context)

def homepage(request):
	return render(request, 'echoes/homepage.html')
