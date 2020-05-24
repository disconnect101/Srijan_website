from django.db import models

# Create your models here.

class YearbookData(models.Model):
    year = models.IntegerField()
    regno = models.IntegerField()
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50,default='Branch')
    aboutme = models.TextField()
    wdysy = models.TextField()
    links = models.TextField()
    souvenir = models.ImageField(upload_to='images/yearbook_souvenirs/')
    photo = models.ImageField(upload_to='images/yearbook_photos/')
    coverphoto = models.ImageField(upload_to='images/yearbook_photos', null=True)

    def __str__(self):
        return str(self.regno)