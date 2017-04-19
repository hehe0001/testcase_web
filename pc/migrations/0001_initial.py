# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-14 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PCTestCase1',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('action', models.CharField(blank=True, max_length=45, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('expected', models.TextField(blank=True, null=True)),
                ('actual', models.TextField(blank=True, editable=False, null=True)),
                ('result', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'p_illness_project_released',
                'verbose_name': 'PC-\u5927\u75c5\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': 'PC-\u5927\u75c5\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='PCTestCase2',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('action', models.CharField(blank=True, max_length=45, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('expected', models.TextField(blank=True, null=True)),
                ('actual', models.TextField(blank=True, editable=False, null=True)),
                ('result', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'p_disaster_project_released',
                'verbose_name': 'PC-\u707e\u96be\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': 'PC-\u707e\u96be\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='PCTestCase3',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('action', models.CharField(blank=True, max_length=45, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('expected', models.TextField(blank=True, null=True)),
                ('actual', models.TextField(blank=True, editable=False, null=True)),
                ('result', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'p_animal_project_released',
                'verbose_name': 'PC-\u52a8\u7269\u4fdd\u62a4\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': 'PC-\u52a8\u7269\u4fdd\u62a4\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='PCTestCase4',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('action', models.CharField(blank=True, max_length=45, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('expected', models.TextField(blank=True, null=True)),
                ('actual', models.TextField(blank=True, editable=False, null=True)),
                ('result', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'p_poverty_project_released',
                'verbose_name': 'PC-\u6276\u8d2b\u52a9\u5b66\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': 'PC-\u6276\u8d2b\u52a9\u5b66\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='PCTestCase5',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('action', models.CharField(blank=True, max_length=45, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('expected', models.TextField(blank=True, null=True)),
                ('actual', models.TextField(blank=True, editable=False, null=True)),
                ('result', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'p_other_project_released',
                'verbose_name': 'PC-\u5176\u4ed6\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': 'PC-\u5176\u5b83\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='PCTestCase6',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('action', models.CharField(blank=True, max_length=45, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('expected', models.TextField(blank=True, null=True)),
                ('actual', models.TextField(blank=True, editable=False, null=True)),
                ('result', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'p_presale_project_released',
                'verbose_name': 'PC-\u5c1d\u9c9c\u9884\u552e\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': 'PC-\u5c1d\u9c9c\u9884\u552e\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='PCTestCase7',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('action', models.CharField(blank=True, max_length=45, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('expected', models.TextField(blank=True, null=True)),
                ('actual', models.TextField(blank=True, editable=False, null=True)),
                ('result', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'p_dream_project_released',
                'verbose_name': 'PC-\u68a6\u60f3\u6e05\u5355\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': 'PC-\u68a6\u60f3\u6e05\u5355\u9879\u76ee\u53d1\u5e03',
            },
        ),
    ]