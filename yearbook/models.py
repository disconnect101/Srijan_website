from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class YearbookData(models.Model):
    year = models.IntegerField(null=True)
    regno = models.IntegerField(null=True)
    name = models.CharField(max_length=50, default=None)
    branch = models.CharField(max_length=50, default=None)
    aboutme = RichTextField(default=None)
    yfm = RichTextField(null=True, blank=True)
    links = RichTextField(null=True, blank=True)
    souvenir = models.ImageField(upload_to='images/yearbook_souvenirs/', null=True, blank=True)
    photo = models.ImageField(upload_to='images/yearbook_photos/', null=True, blank=True)
    coverphoto = models.ImageField(upload_to='images/yearbook_photos/', null=True, blank=True)

    def __str__(self):
        return str(self.regno)
