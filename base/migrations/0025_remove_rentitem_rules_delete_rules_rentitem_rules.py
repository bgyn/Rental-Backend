# Generated by Django 5.1.1 on 2024-12-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_rename_rentitems_booking_rent_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentitem',
            name='rules',
        ),
        migrations.DeleteModel(
            name='Rules',
        ),
        migrations.AddField(
            model_name='rentitem',
            name='rules',
            field=models.TextField(blank=True, null=True),
        ),
    ]
