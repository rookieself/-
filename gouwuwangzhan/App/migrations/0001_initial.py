# Generated by Django 2.1.4 on 2018-12-11 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='axf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255, verbose_name='图片连接地址')),
                ('name', models.CharField(max_length=80, verbose_name='名字')),
                ('trackid', models.CharField(max_length=16, verbose_name='销量')),
            ],
            options={
                'verbose_name': '图片轮播图表',
                'verbose_name_plural': '图片轮播图表',
                'db_table': 'axf_wheel',
            },
        ),
    ]
