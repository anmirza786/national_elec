# Generated by Django 4.0.6 on 2022-08-01 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_category_parent_alter_category_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='ordering',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='catlevel',
            field=models.IntegerField(default=0, verbose_name='Category Level'),
        ),
        migrations.AddField(
            model_name='category',
            name='child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
