# Generated by Django 5.1.1 on 2024-09-18 16:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_donationarea_donation_gallery_volunteer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='creationdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='donationname',
            field=models.CharField(choices=[('Food Donation', 'Food Donation'), ('Cloth Donation', 'Cloth Donation'), ('Footwear Donation', 'Footwear Donation'), ('Furniture Donation', 'Furniture Donation'), ('Books Donation', 'Books Donation'), ('Vessel Donation', 'Vessel Donation'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
