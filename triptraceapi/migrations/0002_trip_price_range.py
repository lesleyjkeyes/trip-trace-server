# Generated by Django 4.1.5 on 2023-01-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triptraceapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='price_range',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]