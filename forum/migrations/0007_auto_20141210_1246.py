# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import datetime
from django.utils.timezone import utc
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('forum', '0006_auto_20141204_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_edited_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 4, 46, 40, 919409, tzinfo=utc), verbose_name='date last edited'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='likes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='top',
            field=models.BooleanField(default=False, verbose_name='Move to top'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_subscribed',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=5000, verbose_name='Content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 4, 46, 40, 919366, tzinfo=utc), auto_now_add=True, verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
