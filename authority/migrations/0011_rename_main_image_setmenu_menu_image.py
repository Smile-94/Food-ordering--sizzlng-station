# Generated by Django 4.1.7 on 2023-03-12 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0010_rename_setmenufood_setmenu_foods_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setmenu',
            old_name='main_image',
            new_name='menu_image',
        ),
    ]