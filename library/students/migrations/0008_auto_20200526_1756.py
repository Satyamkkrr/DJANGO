# Generated by Django 3.0.6 on 2020-05-26 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200526_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbooks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 26, 12, 26, 49, 895771, tzinfo=utc)),
        ),
    ]
