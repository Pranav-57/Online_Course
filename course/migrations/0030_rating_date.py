# Generated by Django 3.1.4 on 2021-01-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0029_auto_20210117_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
