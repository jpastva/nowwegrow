# Generated by Django 2.2.16 on 2020-10-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Business',
            new_name='BusinessType',
        ),
        migrations.RenameField(
            model_name='businesstype',
            old_name='name',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='address1',
            field=models.CharField(default=1, max_length=30, verbose_name='Address Line 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='address2',
            field=models.CharField(default='blank', max_length=30, verbose_name='Address Line 2'),
            preserve_default=False,
        ),
    ]
