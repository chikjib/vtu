# Generated by Django 4.0.2 on 2022-04-17 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_transaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentnotification',
            options={'verbose_name_plural': 'Recent Payment List'},
        ),
        migrations.AlterModelOptions(
            name='servicenotification',
            options={'verbose_name_plural': 'Service Status Notification'},
        ),
        migrations.AddField(
            model_name='paymentnotification',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
