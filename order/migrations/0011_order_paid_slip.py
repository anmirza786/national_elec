# Generated by Django 4.0.5 on 2022-07-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_delete_orderstatusenum_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_slip',
            field=models.FileField(blank=True, upload_to='slips/'),
        ),
    ]
