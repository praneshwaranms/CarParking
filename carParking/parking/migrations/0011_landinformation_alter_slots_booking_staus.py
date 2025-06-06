# Generated by Django 5.0.1 on 2024-01-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0010_alter_slots_booking_staus'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aadhar_number', models.CharField(max_length=12, unique=True)),
                ('document_input', models.FileField(upload_to='documents/')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('landmark_name', models.CharField(max_length=100)),
                ('exact_location', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='slots_booking',
            name='staus',
            field=models.IntegerField(default=0),
        ),
    ]
