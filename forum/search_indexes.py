from django.utils import timezone
from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
	""" The text field is the primary searching field """
	text = indexes.CharField(document=True, use_template=True)
	author = indexes.CharField(model_attr='author')
	pub_date = indexes.DateTimeField(model_attr='pub_date')

	def get_model(self):
		return Post

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(pub_date__lte=timezone.now())