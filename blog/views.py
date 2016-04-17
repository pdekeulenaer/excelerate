from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#definition of main views

def detail(request, blog_id):
	return HttpResponse("Test - %s" % (blog_id))

def index(request):
	return render(request, 'blog/index.html')
	#return HttpResponse("Overview of all blogposts")

def category_index(request, category_id):
	return HttpResponse("Overview of all blogposts in %s" % (category_id))

