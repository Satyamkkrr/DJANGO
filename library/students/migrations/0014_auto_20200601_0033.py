# Generated by Django 3.0.6 on 2020-05-31 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20200529_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbooks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 19, 3, 29, 447774, tzinfo=utc)),
        ),
    ]
