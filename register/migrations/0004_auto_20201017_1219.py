# Generated by Django 2.2.16 on 2020-10-17 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201017_1219'),
        ('orders', '0003_auto_20201017_1219'),
        ('register', '0003_auto_20201016_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='merchant_type',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='user',
        ),
        migrations.DeleteModel(
            name='BusinessType',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Merchant',
        ),
    ]
