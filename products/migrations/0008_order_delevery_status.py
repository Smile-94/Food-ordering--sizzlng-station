# Generated by Django 4.1.7 on 2023-04-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_order_confirmed_at_order_ordered_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delevery_status',
            field=models.BooleanField(default=False),
        ),
    ]