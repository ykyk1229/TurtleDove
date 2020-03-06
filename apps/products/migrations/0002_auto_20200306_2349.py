# Generated by Django 3.0.4 on 2020-03-06 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dev_interface',
            field=models.ManyToManyField(help_text='开发接口人', related_name='dev_interface', to=settings.AUTH_USER_MODEL, verbose_name='开发接口人'),
        ),
        migrations.AddField(
            model_name='product',
            name='op_interface',
            field=models.ManyToManyField(help_text='运维接口人', related_name='op_interface', to=settings.AUTH_USER_MODEL, verbose_name='运维接口人'),
        ),
    ]
