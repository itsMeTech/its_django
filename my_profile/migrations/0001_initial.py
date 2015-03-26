# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('street', models.CharField(max_length=100)),
                ('street_number', models.CharField(max_length=10)),
                ('zip', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(null=True, blank=True, max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('bill', 'Billing'), ('ship', 'Shipping'), ('both', 'Both')], default='both', max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=2)),
                ('title', models.CharField(null=True, max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(null=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
