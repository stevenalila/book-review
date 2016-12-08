from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

class Books(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	summary = models.TextField()
	image = models.CharField(max_length=50) #is this the correct way to store images in the database and is it recommended
	published_date =models.DateTimeField(blank=True, null=True)


	def publish(self): #how is this used
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

#class Reviews(models.Model):
	#author = models.Foreignkey('auth.User') #how do you create a foreign key?

class Comments(models.Model):
	#author = models.Foreignkey('auth.User')
	text = models.TextField()
