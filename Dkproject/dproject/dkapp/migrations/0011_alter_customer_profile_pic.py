# Generated by Django 4.0.6 on 2022-07-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkapp', '0010_customer_profile_pic_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='dkc.png', null=True, upload_to=''),
        ),
    ]