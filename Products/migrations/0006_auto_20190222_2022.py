# Generated by Django 2.1.5 on 2019-02-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_auto_20190222_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageforproduct',
            name='isActive',
        ),
        migrations.RemoveField(
            model_name='imageforproduct',
            name='isMain',
        ),
        migrations.AddField(
            model_name='product',
            name='mainImg',
            field=models.ImageField(default=0, upload_to='static/Shop/img/goods/'),
            preserve_default=False,
        ),
    ]
