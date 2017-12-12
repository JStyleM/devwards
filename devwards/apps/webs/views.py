from django.shortcuts import render

# Create your views here.

def send_website(request):
	return render(request, 'enviar-sitio.html')

def website_detail(request, slug):
	return render(request, 'detalle.html')

def website_vote(request, slug):
	return render(request, 'vote.html')