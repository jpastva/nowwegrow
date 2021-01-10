# Generated by Django 2.2.16 on 2020-10-17 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.CharField(max_length=50, unique=True, verbose_name='Merchant Name')),
                ('merchant_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('merchant_type', models.ManyToManyField(related_name='types_merchant', to='account.BusinessType')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=30, verbose_name='Address Line 1')),
                ('address2', models.CharField(max_length=30, verbose_name='Address Line 2')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('state', models.CharField(max_length=30, verbose_name='State')),
                ('zip', models.CharField(max_length=12, verbose_name='Zip code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]