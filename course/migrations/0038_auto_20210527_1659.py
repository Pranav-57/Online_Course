# Generated by Django 3.1.4 on 2021-05-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0037_auto_20210527_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]