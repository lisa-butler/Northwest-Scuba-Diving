# Generated by Django 3.2 on 2023-01-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_remove_orderlineitem_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='other_qualifications',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
