# Generated by Django 2.0.7 on 2018-08-12 03:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180812_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 12, 3, 49, 41, 18355, tzinfo=utc)),
        ),
    ]