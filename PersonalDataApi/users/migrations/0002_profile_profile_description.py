# Generated by Django 2.1 on 2018-08-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
