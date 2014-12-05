from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class UserProfile(models.Model):
	"""
	Custom user class.
	"""
	user = models.OneToOneField(User)
	avator = models.ImageField(upload_to='profile_image', blank=True)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username

class Post(models.Model):
	title = models.CharField('Title', max_length=120)
	content = RichTextField('Content', max_length=5000)
	pub_date = models.DateTimeField('date published', auto_now_add=True, default=timezone.now())
	tag = models.CharField('Tag', max_length=20)
	author = models.ForeignKey(User)
	thread_post = models.ForeignKey('self', blank=True, null=True)

	def __str__(self):
		return self.title