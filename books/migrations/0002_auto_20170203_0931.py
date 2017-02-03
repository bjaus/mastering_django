# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-publication_date']},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(null=True, max_length=254, blank=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True, verbose_name='Pub Date', blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(null=True, max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='state_province',
            field=models.CharField(max_length=30, verbose_name='State/Province'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.Tag'),
        ),
    ]
