# Generated by Django 3.1.4 on 2021-01-17 07:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_auto_20210117_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
