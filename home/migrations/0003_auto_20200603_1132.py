# Generated by Django 3.0.6 on 2020-06-03 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='timestamp',
            new_name='times',
        ),
    ]
