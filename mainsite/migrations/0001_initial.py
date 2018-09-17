# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-13 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('num', models.IntegerField()),
                ('lasttime', models.DateTimeField()),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Book')),
            ],
            options={
                'db_table': 'browser',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('list1', models.CharField(max_length=255)),
                ('list2', models.CharField(max_length=255)),
                ('list3', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ordertime', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('phonenum', models.CharField(blank=True, max_length=255, null=True)),
                ('finishtime', models.DateTimeField(blank=True, null=True)),
                ('visible', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prices', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Book')),
                ('orderid', models.ForeignKey(db_column='orderid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Order')),
            ],
            options={
                'db_table': 'orderitem',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.IntegerField()),
            ],
            options={
                'db_table': 'phone',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='img')),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Book')),
            ],
            options={
                'db_table': 'picture',
            },
        ),
        migrations.CreateModel(
            name='Presale',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('restnum', models.IntegerField()),
                ('publishtime', models.DateTimeField()),
                ('finishtime', models.DateTimeField()),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Book')),
            ],
            options={
                'db_table': 'presale',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('star', models.DecimalField(decimal_places=2, max_digits=5)),
                ('info', models.CharField(max_length=255)),
                ('publishdate', models.DateTimeField()),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Book')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('purchasetime', models.DateTimeField()),
                ('puchasenum', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prices', models.DecimalField(decimal_places=2, max_digits=15)),
                ('restnum', models.IntegerField()),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Book')),
            ],
            options={
                'db_table': 'storage',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('realname', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Walfare',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Book')),
            ],
            options={
                'db_table': 'walfare',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='userid',
            field=models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.User'),
        ),
        migrations.AddField(
            model_name='phone',
            name='userid',
            field=models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(db_column='buyer', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.User'),
        ),
        migrations.AddField(
            model_name='location',
            name='userid',
            field=models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.User'),
        ),
        migrations.AddField(
            model_name='browser',
            name='userid',
            field=models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='categoryid',
            field=models.ForeignKey(db_column='categoryid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Category'),
        ),
    ]
