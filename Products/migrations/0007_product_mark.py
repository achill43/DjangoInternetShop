# Generated by Django 2.1.5 on 2019-02-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20190222_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mark',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]