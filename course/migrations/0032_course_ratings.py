# Generated by Django 3.1.4 on 2021-05-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0031_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='ratings',
            field=models.IntegerField(default=0),
        ),
    ]
