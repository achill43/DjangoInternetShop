# Generated by Django 2.1.5 on 2019-02-23 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_product_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.ProductMark'),
        ),
    ]
