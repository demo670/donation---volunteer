# Generated by Django 5.1.1 on 2024-09-21 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_gallery_creationdate_alter_donation_donationname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donationdate',
            field=models.DateTimeField(null=True),
        ),
    ]
