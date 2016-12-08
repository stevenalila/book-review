from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	summary = models.TextField()
	image = models.ImageField(blank=True, null=True, upload_to="uploads/books/thumbnails/") #is this the correct way to store images in the database and is it recommended
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

class BookReview(models.Model):
	author = models.ForeignKey('auth.User', related_name='reviews') #how do you create a foreign key?

class Comment(models.Model):
	author = models.ForeignKey('auth.User', related_name='comments')
	review = models.ForeignKey('Review', related_name='comments')
	timestamp = models.DateTimeField(auto_now_add=True)	
	text = models.TextField()
