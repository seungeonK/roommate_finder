# Generated by Django 3.1.7 on 2021-03-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210326_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='graduation_year',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]
