# Generated by Django 5.0.1 on 2024-01-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_slots_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='anything',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing', models.CharField(default='-', max_length=50)),
            ],
        ),
    ]
