# Generated by Django 3.1.2 on 2020-10-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20201011_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='password',
            new_name='phone',
        ),
    ]
