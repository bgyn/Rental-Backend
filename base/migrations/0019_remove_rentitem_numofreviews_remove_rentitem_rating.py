# Generated by Django 5.1.1 on 2024-12-21 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_rename_userid_rentitem_users_userlisting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentitem',
            name='numOfReviews',
        ),
        migrations.RemoveField(
            model_name='rentitem',
            name='rating',
        ),
    ]
