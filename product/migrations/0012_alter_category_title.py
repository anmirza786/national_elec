# Generated by Django 4.0.6 on 2022-08-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Sub Category'),
        ),
    ]
