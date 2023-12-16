# Generated by Django 4.2.6 on 2023-11-24 07:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0017_remove_question_starred_alter_post_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hangul_title', models.CharField(default='신쳔지', max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('start_date', models.IntegerField(default=1983)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 11, 24, 7, 26, 24, 873221, tzinfo=datetime.timezone.utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 7, 26, 24, 872275, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='DM',
        ),
    ]
