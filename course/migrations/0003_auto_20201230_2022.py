# Generated by Django 3.1.4 on 2020-12-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_coursecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='course_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
