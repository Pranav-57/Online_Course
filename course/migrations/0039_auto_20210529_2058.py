# Generated by Django 3.1.4 on 2021-05-29 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0038_auto_20210527_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='course.course'),
        ),
    ]
