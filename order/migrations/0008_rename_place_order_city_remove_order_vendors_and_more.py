# Generated by Django 4.0.5 on 2022-07-15 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_orderitem_order_alter_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='place',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='vendors',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='vendor_paid',
        ),
    ]
