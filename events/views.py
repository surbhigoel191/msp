from django.shortcuts import render, HttpResponse, redirect
from .models import Candidate
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .forms import PostForm
from .forms import QuesForm
# Create your views here.
def login(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		try:
			validate_email(email)
		except ValidationError:
			print ("oops! wrong email")
		if form.is_valid():
			form.save()
			login(request, user)
			return redirect('instructions')
	else:
		form = PostForm()
	return render(request, 'events/login.html', {'form': form})
def welcome(request):
	return render(request,'events/welcome.html')
def test(request):  
	return render(request,'events/test.html')
def instructions(request):
	return render(request,'events/instructions.html')
