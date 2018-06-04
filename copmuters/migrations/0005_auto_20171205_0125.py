# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('copmuters', '0004_auto_20171125_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='BelongTO',
            fields=[
                ('quantity', models.IntegerField(null=True)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('price', models.IntegerField(default=0, null=True)),
                ('description', models.TextField(default='No description yet', max_length=500)),
                ('type', models.CharField(choices=[('Monoblock', 'Monoblock'), ('Personal Computer', 'Personal computer'), ('Laptop', 'Laptop')], default='Personal Computer', max_length=30)),
                ('pic', models.ImageField(blank=True, max_length=1000, upload_to='media/')),
                ('quantity', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.AutoField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_open', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copmuters.Customer')),
                ('items', models.ManyToManyField(through='copmuters.BelongTO', to='copmuters.Computer')),
            ],
        ),
        migrations.RemoveField(
            model_name='usluga',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usluga',
            name='user_zakaz',
        ),
        migrations.DeleteModel(
            name='Usluga',
        ),
        migrations.DeleteModel(
            name='zakaz',
        ),
        migrations.AddField(
            model_name='belongto',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copmuters.Computer'),
        ),
        migrations.AddField(
            model_name='belongto',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copmuters.Order'),
        ),
    ]