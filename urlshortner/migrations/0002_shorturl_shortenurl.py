# Generated by Django 2.1.7 on 2019-04-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='shortenurl',
            field=models.CharField(default='qwerty', max_length=50),
        ),
    ]
