# Generated by Django 3.1.4 on 2021-01-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20210102_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='resourse',
            new_name='resource',
        ),
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
