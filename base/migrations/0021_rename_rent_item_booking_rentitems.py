# Generated by Django 5.1.1 on 2024-12-22 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_booking_delete_userlisting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='rent_item',
            new_name='rentItems',
        ),
    ]
