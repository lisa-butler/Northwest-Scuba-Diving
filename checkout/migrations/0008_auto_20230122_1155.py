# Generated by Django 3.2 on 2023-01-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_other_qualifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='other_qualifications',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='diver_age',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='diver_grade',
            new_name='street_address2',
        ),
        migrations.AddField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
