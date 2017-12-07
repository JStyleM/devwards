from django.shortcuts import render

# Create your views here.

def send_website(request):
	return render(request, 'enviar-sitio.html')

def website_detail(request):
	return render(request, 'detalle.html')

def website_vote(request):
	return render(request, 'vote.html')