# Generated by Django 2.2.6 on 2019-11-08 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
