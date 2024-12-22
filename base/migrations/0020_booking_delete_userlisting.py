# Generated by Django 5.1.1 on 2024-12-22 06:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_remove_rentitem_numofreviews_remove_rentitem_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('notAccepted', 'notAccepted')], default='pending', max_length=200)),
                ('total_price', models.CharField(blank=True, max_length=30, null=True)),
                ('rent_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='base.rentitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserListing',
        ),
    ]