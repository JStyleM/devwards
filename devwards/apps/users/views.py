from django.shortcuts import render

# Create your views here.

def register(request):
	return render(request, 'register.html')

def login_user(request):
	return render(request, 'login.html')