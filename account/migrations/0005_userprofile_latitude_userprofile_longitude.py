# Generated by Django 5.1.1 on 2024-12-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='latitude',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='longitude',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]