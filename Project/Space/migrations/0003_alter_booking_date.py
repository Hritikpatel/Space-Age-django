# Generated by Django 4.1 on 2022-10-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0002_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
