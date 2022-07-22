# Generated by Django 4.0.5 on 2022-07-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularClients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='clients')),
                ('ratting', models.PositiveIntegerField(verbose_name='Client`s Ratting')),
            ],
        ),
    ]
