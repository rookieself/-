# Generated by Django 2.1.4 on 2018-12-11 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_mainshow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainshow',
            options={'verbose_name': '商品展示', 'verbose_name_plural': '商品展示'},
        ),
        migrations.AlterModelTable(
            name='mainshow',
            table='axf_mainshow',
        ),
    ]