# Generated by Django 5.0.1 on 2024-01-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0012_alter_landinformation_aadhar_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landinformation',
            name='aadhar_number',
            field=models.CharField(max_length=100),
        ),
    ]
