# Generated by Django 5.0.4 on 2024-04-06 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='st',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='alumni.category'),
        ),
    ]