# Generated by Django 5.1.4 on 2025-03-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='suitable_environment',
            field=models.TextField(default='Information about suitable growing condition will be added soon'),
        ),
    ]
