# Generated by Django 4.1.7 on 2023-04-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customermessage_send_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermessage',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
