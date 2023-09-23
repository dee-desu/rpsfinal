# Generated by Django 4.2.5 on 2023-09-22 11:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_bannerimage_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='locations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
    ]
