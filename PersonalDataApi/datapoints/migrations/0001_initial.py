# Generated by Django 2.0.7 on 2018-07-17 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('category', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='datapoints/images')),
                ('audio', models.FileField(blank=True, null=True, upload_to='datapoints/audio')),
                ('source_device', models.TextField()),
                ('value', models.FloatField(blank=True)),
                ('text_from_audio', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]