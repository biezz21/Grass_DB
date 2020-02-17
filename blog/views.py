from django.shortcuts import render
from .models import grass_db
from django import forms

# Create your views here.

def post_list(request):
	
	Posts = grass_db.objects.all()
	query = request.GET.get("q")
	post_data 		= grass_db.objects.filter(Common_N=query)

	return_source 	=  {'query':query, 'Posts':Posts, 'post_data':post_data}

	
	return render(request, 'blog/post_list.html', return_source)
