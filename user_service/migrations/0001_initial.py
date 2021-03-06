# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBilling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan', models.CharField(default=b'FREE', max_length=10, choices=[(b'FREE', 'Free'), (b'PAY_PER_USE', 'Pay_Per_Use'), (b'MONTHLY', 'Monthly'), (b'QUARTERLY', 'Quarterly'), (b'YEARLY', 'Yearly')])),
                ('is_plan_active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2015, 4, 16, 11, 30, 34, 837998))),
                ('date_updated', models.DateTimeField(default=datetime.datetime(2015, 4, 16, 11, 30, 34, 838022), blank=True)),
                ('quota_available', models.IntegerField(default=0)),
                ('quota_utilized', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('phone_number', models.CharField(default=b'', max_length=b'50', blank=True)),
                ('title', models.CharField(default=b'', max_length=b'50', blank=True)),
                ('company', models.CharField(default=b'', max_length=b'50', blank=True)),
                ('status', models.CharField(default=b'UNKNOWN', max_length=10, choices=[(b'UNKNOWN', 'Unknown'), (b'INVITED', 'Invitation Sent (only email known)'), (b'IDENTIFIED', 'Identified (email and name known)'), (b'VERIFIED', 'Verified e-mail address'), (b'USER', 'Signed Up')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
