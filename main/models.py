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

