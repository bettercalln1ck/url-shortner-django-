# Generated by Django 2.1.7 on 2019-04-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0004_auto_20190405_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortenurl',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]