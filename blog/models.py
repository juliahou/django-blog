from django.db import models
from django.utils import timezone

# Create your models here.

#defining django model Post
class Post(models.Model):
	#models.ForeignKey is a link to another model
	author = models.ForeignKey('auth.User')
	#models.CharField defines text with limited number of characters
	title = models.CharField(max_length=200)
	#models.TextField defines long text without a limit
	text = models.TextField()
	#models.DateTimeField defines a date and time
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
