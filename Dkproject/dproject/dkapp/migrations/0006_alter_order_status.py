# Generated by Django 4.0.6 on 2022-07-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkapp', '0005_remove_order_tag_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered ', 'Delivered'), ('Pending', 'Pending')], max_length=200),
        ),
    ]
