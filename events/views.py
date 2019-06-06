from django.shortcuts import render, HttpResponse


# Create your views here.
def login(request):
	return render(request,'events/login.html')
def welcome(request):
	return render(request,'events/welcome.html')
def test(request):
	return HttpResponse('Test!')