# Generated by Django 3.2 on 2023-01-11 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='name',
        ),
    ]
