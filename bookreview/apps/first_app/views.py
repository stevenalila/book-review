from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import BookReviewForm


# Create your views here.
def index(request):
	return render(request, "first_app/index.html")

def registration(request):
	return render(request, "first_app/registration.html")

def login(request):
	return render(request, "first_app/login.html")

@login_required
def reviews(request):
	return render(request, "first_app/reviews.html")

@login_required
def review(request):
    return render(request, "first_app/review.html")

@login_required
def create_review(request):
    form = BookReviewForm()

    if request.method == 'POST':
        form = BookReviewForm(request.POST)

        if form.is_valid():
            # form.instance = BookReview([form_parameters]) 
            book_review = form.instance
            book_review.user = request.user
            book_review.save()
            return HttpResponseRedirect(book_review.get_absolute_url())

    return render(request, "first_app/create_review.html", {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(BookReview, id=review_id)
    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect('/reviews/')
        
    return render(request, "first_app/delete_review.html")

def comments(request):
	return render(request, "first_app/comments.html")
