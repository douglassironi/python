# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='reservas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField(auto_now=True)),
                ('reservista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.pessoas')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='salao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Salao',
                'verbose_name_plural': 'Saloes',
            },
        ),
        migrations.AddField(
            model_name='reservas',
            name='salao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.salao'),
        ),
    ]