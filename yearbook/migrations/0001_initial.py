# Generated by Django 3.0.3 on 2020-06-17 11:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YearbookData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('regno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('aboutme', ckeditor.fields.RichTextField()),
                ('yfm', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('links', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('souvenir', models.ImageField(blank=True, null=True, upload_to='images/yearbook_souvenirs/')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/yearbook_photos/')),
                ('coverphoto', models.ImageField(blank=True, null=True, upload_to='images/yearbook_photos/')),
            ],
        ),
    ]
