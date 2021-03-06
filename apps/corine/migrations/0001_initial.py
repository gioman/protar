# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 22:18
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('grid_code', models.IntegerField()),
                ('label_1', models.CharField(max_length=100)),
                ('label_2', models.CharField(max_length=100)),
                ('label_3', models.CharField(max_length=100)),
                ('color', models.CharField(default='', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Patch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('clcid', models.TextField()),
                ('year', models.IntegerField()),
                ('change', models.BooleanField()),
                ('change_type', models.CharField(max_length=10, null=True)),
                ('remark', models.TextField()),
                ('area_ha', models.FloatField()),
                ('shape_length', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=3035)),
                ('nomenclature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corine.Nomenclature')),
                ('nomenclature_previous', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous_patches', to='corine.Nomenclature')),
            ],
            options={
                'verbose_name_plural': 'patches',
            },
        ),
    ]
