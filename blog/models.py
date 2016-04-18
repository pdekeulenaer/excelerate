from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=500, unique=True)
	title_slug = models.SlugField(max_length=500, unique=True)
	publication_date = models.DateTimeField('date created', auto_now_add=True)
	published = models.BooleanField(default=False, blank=False)
	content = models.TextField()

	author = models.ForeignKey(User, default=None)
	category = models.ForeignKey('blog.Category')

	def __str__(self):
		return '%s' % (self.title)


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=500)

	parent_category = models.ForeignKey('blog.Category', default=None, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.name)

class Comment(models.Model):
	text = models.CharField(max_length=1000)
	creation_date = models.DateTimeField('date created', auto_now_add=True)
	
	parent_post = models.ForeignKey('blog.Post', default=None, blank=False, null=False)
	author = models.ForeignKey(User, default=None, blank=True)

	def __str__(self):
		return '%s' % (self.text)
