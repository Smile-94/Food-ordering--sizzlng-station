# Generated by Django 4.1.7 on 2023-04-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0003_shippingcharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingcharge',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shippingcharge',
            name='modified_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shippingcharge',
            name='shipping_charge',
            field=models.IntegerField(),
        ),
    ]