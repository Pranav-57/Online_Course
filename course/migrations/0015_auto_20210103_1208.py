# Generated by Django 3.1.4 on 2021-01-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20210103_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.CharField(max_length=10, null=True),
        ),
    ]