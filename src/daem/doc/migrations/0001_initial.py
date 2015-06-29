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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, blank=True, max_length=120)),
                ('discipline', models.CharField(null=True, blank=True, max_length=120)),
                ('professor', models.CharField(null=True, blank=True, max_length=120)),
            ],
        ),
    ]
