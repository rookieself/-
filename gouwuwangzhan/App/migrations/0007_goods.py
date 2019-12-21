# Generated by Django 2.1.4 on 2018-12-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20181211_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(default=1)),
                ('productimg', models.CharField(max_length=255)),
                ('productname', models.CharField(max_length=255)),
                ('productlongname', models.CharField(max_length=255)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.BooleanField(default=False)),
                ('specifics', models.CharField(max_length=80)),
                ('price', models.FloatField(default=0)),
                ('marketprice', models.FloatField(default=0)),
                ('categoryid', models.IntegerField(default=1)),
                ('childcid', models.IntegerField(default=1)),
                ('childcidname', models.CharField(max_length=255)),
                ('dealerid', models.IntegerField(default=1)),
                ('storenums', models.IntegerField(default=1)),
                ('productnum', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': '商品信息表',
                'verbose_name_plural': '商品信息表',
                'db_table': 'axf_goods',
            },
        ),
    ]
