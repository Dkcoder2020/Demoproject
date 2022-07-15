# Generated by Django 4.0.6 on 2022-07-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkapp', '0009_customer_user_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out of delivery', 'Out of delivery'), ('Delivereds', 'Delivereds')], max_length=200),
        ),
    ]
