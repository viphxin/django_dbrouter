# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewlyUserServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='\u7528\u6237\u552f\u4e00ID')),
                ('date_log', models.DateTimeField(auto_now_add=True, verbose_name='\u6700\u540e\u767b\u9646\u65e5\u671f')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameserver.ServerGroup')),
            ],
            options={
                'db_table': 'newlyuserserver',
                'verbose_name': '\u7528\u6237\u6700\u8fd1\u767b\u9646\u670d\u52a1\u5668',
                'verbose_name_plural': '\u7528\u6237\u6700\u8fd1\u767b\u9646\u670d\u52a1\u5668',
            },
        ),
    ]
