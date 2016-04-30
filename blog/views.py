from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Post


#definition of main views

def detail(request, blog_id):
	p = Post.objects.get(id=blog_id)
	return render(request, 'blog/post_detail.html', {'post':p})

def index(request):
	#show top 5 blog posts
	posts = Post.objects.filter(published=True).order_by('-publication_date')
	
	return render(request, 'blog/index.html', {'posts' : posts[:3]})


def category_index(request, category_id):
	return render(request, 'blog/test.html')

