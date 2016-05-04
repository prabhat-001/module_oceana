# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GuestPassport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passphoto', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Guest')),
            ],
        ),
    ]
