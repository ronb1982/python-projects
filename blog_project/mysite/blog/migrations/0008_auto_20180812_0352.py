# Generated by Django 2.0.7 on 2018-08-12 03:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180812_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 12, 3, 52, 42, 971171, tzinfo=utc)),
        ),
    ]
