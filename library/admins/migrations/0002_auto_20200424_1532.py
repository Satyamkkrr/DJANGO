# Generated by Django 3.0.5 on 2020-04-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_librarian',
            name='contact',
            field=models.PositiveIntegerField(),
        ),
    ]