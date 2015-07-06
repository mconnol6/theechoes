from django.shortcuts import render

def performances(request):
	return render(request, 'echoes/performances.html')

def homepage(request):
	return render(request, 'echoes/homepage.html')
