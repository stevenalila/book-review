from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'), #url expression where 127.0.0.1:8000/index leads to website
	url(r'^login$', views.login, name='login'), #url expression where 127.0.0.1:8000/login leads to website
	url(r'^reviews$', views.reviews, name='reviews'),
	url(r'^registration$', views.registration, name='registration'), 
	url(r'^comments$', views.comments, name='comments'),
	

]