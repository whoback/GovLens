# Generated by Django 2.2 on 2019-04-23 23:30

import apps.civic_pulse.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic_pulse', '0004_bunch_of_boolean_flags'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='agency',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='agency',
            name='last_successful_scrape',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='latitude',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='agency',
            name='logo',
            field=models.ImageField(blank=True, upload_to=apps.civic_pulse.models.logo_path),
        ),
        migrations.AddField(
            model_name='agency',
            name='longitude',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='agency',
            name='scrape_counter',
            field=models.IntegerField(default=0),
        ),
    ]
