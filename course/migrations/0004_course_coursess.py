# Generated by Django 3.1.4 on 2020-12-30 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20201230_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='coursess',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='course.coursecategory'),
        ),
    ]
