# Generated by Django 5.1.1 on 2024-12-22 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_rename_users_rentitem_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='rentItems',
            new_name='rent_item',
        ),
    ]
