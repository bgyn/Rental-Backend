# Generated by Django 5.1.1 on 2024-12-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_date_of_birth_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
