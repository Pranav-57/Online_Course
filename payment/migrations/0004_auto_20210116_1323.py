# Generated by Django 3.1.4 on 2021-01-16 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20210116_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=50),
        ),
    ]
