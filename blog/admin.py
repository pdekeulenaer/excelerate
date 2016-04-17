from django.contrib import admin
from blog.models import Post, Category, Comment


# Setting some default values
class PostAdmin(admin.ModelAdmin):
	exclude = ['publication_date', 'author']
	prepopulated_fields = {'title_slug':('title',)}

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)