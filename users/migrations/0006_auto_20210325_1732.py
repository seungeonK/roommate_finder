# Generated by Django 3.1.7 on 2021-03-25 21:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210325_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='graduation_year',
            field=models.IntegerField(blank=True, default=2021, validators=[django.core.validators.MinValueValidator(2021)]),
        ),
    ]
