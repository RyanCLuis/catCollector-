from django.urls import path
from . import views

# this file is how we map our urls to views
# views are like our controllers, they map HTTP requests to code. This file is how we match those requests to specific urls.
# the line 'name='home'' is a kwarg, which gives the route a name. naming routes is optional, but best practices.
# later in the codealong, we'll see just how useful it is to name out routes
urlpatterns = [
    # first arg - url endpoint
    # sec arg - the view to render
    # third arg(opt) - names the route 
	path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('cats/', views.cats_index, name = 'index')
]