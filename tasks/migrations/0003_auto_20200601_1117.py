# Generated by Django 2.2.10 on 2020-06-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200530_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='high_priority',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='low_priority',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='medium_priority',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='todo_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
