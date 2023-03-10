# Generated by Django 4.1.5 on 2023-01-25 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha2', models.CharField(max_length=10)),
                ('alpha3', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('duration_unit', models.CharField(max_length=25)),
                ('price_range', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.country')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('about', models.CharField(max_length=400)),
                ('image_url', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_url', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('duration', models.CharField(max_length=10)),
                ('duration_unit', models.CharField(max_length=25)),
                ('region', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('public', models.BooleanField(default=False)),
                ('price_range', models.CharField(max_length=10)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.country')),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='StopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.category')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.stop')),
            ],
        ),
        migrations.AddField(
            model_name='stop',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.trip'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.user')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triptraceapi.trip')),
            ],
        ),
    ]
