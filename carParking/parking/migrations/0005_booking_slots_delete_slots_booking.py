# Generated by Django 5.0.1 on 2024-01-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_delete_anything'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='slots_booking',
        ),
    ]
