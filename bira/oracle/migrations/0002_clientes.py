# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('enderecos', models.CharField(max_length=100)),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oracle.database')),
            ],
        ),
    ]