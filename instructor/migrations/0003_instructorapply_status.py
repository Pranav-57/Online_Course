# Generated by Django 3.1.4 on 2021-05-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_auto_20210523_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructorapply',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=30),
        ),
    ]
