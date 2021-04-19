# Generated by Django 3.1.7 on 2021-04-15 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_profile_match_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='on_grounds',
            field=models.CharField(blank=True, choices=[('on-grounds', 'On-Grounds'), ('off-grounds', 'Off-Grounds'), ('no preference', 'No Preference'), ('na', 'N/A')], max_length=50),
        ),
    ]