# Generated by Django 5.1.1 on 2024-10-07 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_latiude_rentitem_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentitem',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.categories'),
            preserve_default=False,
        ),
    ]
