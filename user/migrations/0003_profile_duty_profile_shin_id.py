# Generated by Django 4.2.6 on 2023-11-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='duty',
            field=models.CharField(default='신쳔지', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='shin_id',
            field=models.CharField(default='SCJ00000000', max_length=20),
        ),
    ]
