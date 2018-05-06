# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bcover_img', models.CharField(max_length=200)),
                ('bauthor', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField()),
            ],
        ),
    ]
