# Generated by Django 4.2.6 on 2023-11-20 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 19, 16, 21, 575222, tzinfo=datetime.timezone.utc)),
        ),
    ]