from django.db import models
from django.utils import timezone


class Articles(models.Model):
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=100)
	content = models.TextField()
	description = models.TextField(null=True,blank=True)

	CATEGORIES = (
		('com', 'committees'),
		('intd', 'Intern Diaries'),
		('als', 'Alumsays'),
	)

	category = models.CharField(max_length=50, choices=CATEGORIES)
	date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.title

