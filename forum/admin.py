from django.contrib import admin
from .models import Post, UserProfile
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'pub_date', 'tag', 'author', 'thread_post')
	readonly_fields = ('pub_date', 'thread_post')
	fieldsets = [
		(None,    {'fields':['title']}),
		('Content', {'fields':['content']}),
		('Published date', {'fields':['pub_date'], 'classes':['collapse']}),
		('Tag', {'fields':['tag']}),
		('Author', {'fields':['author']})
	]

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)