# Generated by Django 3.1.4 on 2021-01-13 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]