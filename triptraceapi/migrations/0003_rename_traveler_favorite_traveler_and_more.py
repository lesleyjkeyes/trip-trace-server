# Generated by Django 4.1.5 on 2023-01-18 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triptraceapi', '0002_trip_price_range'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='Traveler',
            new_name='traveler',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='Trip',
            new_name='trip',
        ),
    ]
