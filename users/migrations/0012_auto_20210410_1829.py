# Generated by Django 3.1.7 on 2021-04-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210409_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_profile',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='display_property',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]