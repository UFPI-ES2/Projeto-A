# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_section_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='app',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
