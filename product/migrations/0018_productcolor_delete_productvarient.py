# Generated by Django 4.0.6 on 2022-09-26 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_remove_product_main_varient'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varient', models.CharField(blank=True, max_length=255, null=True, verbose_name='Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='varients', to='product.product')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductVarient',
        ),
    ]