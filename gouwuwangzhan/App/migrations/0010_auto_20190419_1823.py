# Generated by Django 2.1.7 on 2019-04-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axfuser',
            name='email',
            field=models.CharField(max_length=70),
        ),
    ]
