# Generated by Django 4.0.2 on 2022-04-17 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_services', '0003_airtelproductlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airtelproductlist',
            options={'verbose_name_plural': 'Airtel Datashare Product List'},
        ),
        migrations.AlterModelOptions(
            name='productlist',
            options={'verbose_name_plural': 'Mtn Datashare Product List'},
        ),
    ]
