from django.shortcuts import render

def index(request):
	return render(request, 'echoes/index.html')
