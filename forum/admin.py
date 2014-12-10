from django.contrib import admin
from .models import Post, UserProfile
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'pub_date', 'get_tags', 'tag', 'author', 'last_edited_date', 'thread_post')
	readonly_fields = ('pub_date', 'last_edited_date', 'thread_post')
	fieldsets = [
		(None,    {'fields':['title']}),
		('Content', {'fields':['content']}),
		('Published date', {'fields':['pub_date'], 'classes':['collapse']}),
		('Laste modified date', {'fields':['last_edited_date'], 'classes':['collapse']}),
		('Tags', {'fields':['tags']}),
		('Unused Tag field', {'fields':['tag']}),
		('Author', {'fields':['author']})
	]

	def get_tags(self, post):
		tags = []
		for tag in post.tags.all():
			tags.append(str(tag))
		return ', '.join(tags)

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)