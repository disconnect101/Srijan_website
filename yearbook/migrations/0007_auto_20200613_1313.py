# Generated by Django 3.0.3 on 2020-06-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0006_auto_20200613_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearbookdata',
            name='coverphoto',
            field=models.ImageField(blank=True, null=True, upload_to='images/yearbook_photos'),
        ),
        migrations.AlterField(
            model_name='yearbookdata',
            name='links',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yearbookdata',
            name='souvenir',
            field=models.ImageField(blank=True, null=True, upload_to='images/yearbook_souvenirs/'),
        ),
        migrations.AlterField(
            model_name='yearbookdata',
            name='wdysy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yearbookdata',
            name='yfm',
            field=models.TextField(blank=True, null=True),
        ),
    ]
