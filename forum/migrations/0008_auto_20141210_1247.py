# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20141210_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_edited_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 4, 47, 17, 847864, tzinfo=utc), verbose_name='date last edited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 4, 47, 17, 847823, tzinfo=utc), auto_now_add=True, verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
