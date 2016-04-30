from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



#definition of main views

def detail(request, blog_id):
	p = Post.objects.get(id=blog_id)
	return render(request, 'blog/post_detail.html', {'post':p})

def index(request):
	# set category
	category = request.GET.get('cat')
	print category

	# show top 5 blog posts
	if (category is None):
		posts = Post.objects.filter(published=True).order_by('-publication_date')
	else:
		posts = Post.objects.filter(published=True, category__name=category).order_by('-publication_date')

	# Pagination
	pgtr = Paginator(posts, 2)
	page = request.GET.get('page')


	try:
		posts = pgtr.page(page)
	except PageNotAnInteger:
		posts = pgtr.page(1)
	except EmptyPage:
		posts = pgtr.page(pgtr.num_pages)

	return render(request, 'blog/index.html', {'posts' : posts})


def category_index(request, category_id):
	return render(request, 'blog/test.html')

