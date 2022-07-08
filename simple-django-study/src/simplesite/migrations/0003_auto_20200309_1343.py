# Generated by Django 3.0.4 on 2020-03-09 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('simplesite', '0002_auto_20200309_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='slug',
            new_name='category_slug',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 16, 43, 8, 807687, tzinfo=utc), verbose_name='Date'),
        ),
    ]