# Generated by Django 4.2.6 on 2023-11-17 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_post_delete_memorize'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hangul_title',
            field=models.CharField(default='신쳔지', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 9, 58, 4, 997136, tzinfo=datetime.timezone.utc)),
        ),
    ]
