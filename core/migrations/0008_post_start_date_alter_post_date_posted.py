# Generated by Django 4.2.6 on 2023-11-17 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_post_hangul_title_alter_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.IntegerField(default=1983),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 11, 24, 18, 428396, tzinfo=datetime.timezone.utc)),
        ),
    ]