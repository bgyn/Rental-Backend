# Generated by Django 5.1.1 on 2024-12-21 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rentitem_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentitem',
            old_name='users',
            new_name='userId',
        ),
    ]
