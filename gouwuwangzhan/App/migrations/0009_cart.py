# Generated by Django 2.1.4 on 2018-12-15 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_axfuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('is_select', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.AXFUser')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'cart',
            },
        ),
    ]