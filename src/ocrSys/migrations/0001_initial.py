# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=120, null=True, blank=True)),
                ('discipline', models.CharField(max_length=120, null=True, blank=True)),
                ('professor', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
    ]
