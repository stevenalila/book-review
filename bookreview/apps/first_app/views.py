from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "first_app/index.html")

def registration(request):
	return render(request, "first_app/registration.html")

def login(request):
	return render(request, "first_app/login.html")

def reviews(request):
	return render(request, "first_app/reviews.html")

def comments(request):
	return render(request, "first_app/comments.html")
