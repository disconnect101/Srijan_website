from django.db import models
from django.utils import timezone


class Articles(models.Model):
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=100)
	content = models.TextField()
	description = models.TextField(null=True,blank=True)

	"""
	
	aritcle categories:
	 campus: campus
	 career: intern diaries, alumsays, competetive exams
	 sound of silence: sound of silence
	 
	"""

	CATEGORIES = (
		('cmp', 'campus'),
		('intd', 'Intern Diaries'),
		('als', 'Alumsays'),
		('compe', 'competetive exams'),
		('sos', 'sound of silence'),
	)

	category = models.CharField(max_length=50, choices=CATEGORIES)
	date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	comment = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.firstname

class ArticleImages(models.Model):
	article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/', null=True, blank=True)

class Publications(models.Model):
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=50)
	description = models.TextField()
	cover_image = models.ImageField(upload_to='images/', null=True, blank=True)
	file = models.FileField(upload_to='publications/')
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class FeaturedImages(models.Model):
	image = models.ImageField(upload_to='images/featured_images/', null=True, blank=True)
	about = models.TextField(null=True, blank=True)

class Contributors(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/contributors/', null=True, blank=True)
	year = models.IntegerField()
	branch = models.CharField(max_length=50)

	def __str__(self):
		return self.name





