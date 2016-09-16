# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('about', models.TextField(null=True, blank=True)),
                ('github_url', models.URLField(max_length=250, null=True, blank=True)),
                ('twitter_url', models.URLField(max_length=250, null=True, blank=True)),
                ('facebook_url', models.URLField(max_length=250, null=True, blank=True)),
                ('linkedin_url', models.URLField(max_length=250, null=True, blank=True)),
                ('website', models.URLField(max_length=250, null=True, blank=True)),
                ('skype_id', models.CharField(max_length=250, null=True, blank=True)),
                ('phone', models.CharField(max_length=10, null=True, blank=True)),
                ('template', models.BooleanField(default=1)),
                ('extra', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together=set([('email',)]),
        ),
    ]
