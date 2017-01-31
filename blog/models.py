from django.db import models
from django.utils import timezone

class Category(models.Model):
		name = models.CharField(max_length=100)

		def __str__(self):
			return self.name

class Post(models.Model):
		author = models.ForeignKey('auth.User')
		title = models.CharField(max_length=200)
		text = models.TextField()
		created_date = models.DateTimeField(
			default=timezone.now)
		published_date = models.DateTimeField(
			blank=True, null=True)

		def publish(self):
			self.published_date = timezone.now()
			self.save()

		def __str__(self):
			return self.title

class Comment(models.Model):
		post = models.ForeignKey(Post, related_name='comments')
		user = models.CharField(max_length=250)
		email = models.EmailField()
		body = models.TextField()
		created = models.DateTimeField(auto_now_add=True)
		approved = models.BooleanField(default=False)

		def approved(self):
			self.approved=True
			self.save()

		def __str__(self):
			return self.user

class Place(models.Model):
		name = models.CharField(max_length=200)
		parametr = models.CharField(max_length=15)
		text = models.TextField()

		def __str__(self):
			return self.name

class Attraction(models.Model):
		place = models.ForeignKey(Place, related_name='attractions')
		category = models.CharField(max_length=250)
		body = models.TextField()