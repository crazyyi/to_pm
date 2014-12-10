from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.
class UserProfile(models.Model):
	"""
	Custom user class.
	"""
	user = models.OneToOneField(User)
	avator = models.ImageField(upload_to='profile_image', blank=True)
	is_subscribed = models.BooleanField(default=True)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username

class Post(models.Model):
	title = models.CharField('标题', max_length=120)
	content = RichTextField('内容', max_length=5000)
	pub_date = models.DateTimeField('date published', auto_now_add=True, default=timezone.now())
	last_edited_date = models.DateTimeField('date last edited', default=timezone.now())
	likes = models.IntegerField('喜欢', default=0)
	top = models.BooleanField('Move to top', default=False)
	tag = models.CharField(max_length=20)
	tags = TaggableManager(verbose_name='标签')
	is_active = models.BooleanField('Is active', default=True)
	author = models.ForeignKey(User)
	thread_post = models.ForeignKey('self', blank=True, null=True)

	def __str__(self):
		return self.title