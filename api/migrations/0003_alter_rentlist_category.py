# Generated by Django 5.0.7 on 2024-08-25 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rentlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentlist',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.category'),
        ),
    ]
