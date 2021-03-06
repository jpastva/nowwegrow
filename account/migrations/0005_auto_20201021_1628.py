# Generated by Django 2.2.16 on 2020-10-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201021_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstype',
            options={'ordering': ('type',), 'verbose_name': 'type', 'verbose_name_plural': 'types'},
        ),
        migrations.AddField(
            model_name='businesstype',
            name='slug',
            field=models.SlugField(default='blank', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='merchantprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='merchantprofile',
            name='merchant_email',
            field=models.EmailField(blank=True, max_length=75),
        ),
    ]
