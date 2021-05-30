# Generated by Django 3.1.4 on 2021-01-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]