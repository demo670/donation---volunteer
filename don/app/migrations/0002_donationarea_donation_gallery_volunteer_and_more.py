# Generated by Django 5.1.1 on 2024-09-15 20:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('creationdate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationname', models.CharField(max_length=100, null=True)),
                ('donationpic', models.ImageField(blank=True, null=True, upload_to='donation')),
                ('collectionloc', models.CharField(max_length=300, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('donationdate', models.ImageField(null=True, upload_to='')),
                ('adminremark', models.CharField(max_length=200, null=True)),
                ('volunteerremark', models.CharField(max_length=200, null=True)),
                ('updationdate', models.DateField(null=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.donor')),
                ('donationarea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.donationarea')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverypic', models.FileField(null=True, upload_to='')),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.donation')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='volunteer')),
                ('idpic', models.ImageField(blank=True, null=True, upload_to='volunteer')),
                ('aboutme', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('regdate', models.DateField(auto_now_add=True)),
                ('adminremark', models.CharField(max_length=500, null=True)),
                ('updationdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='volunteer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.volunteer'),
        ),
    ]
