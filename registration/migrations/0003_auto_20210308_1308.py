# Generated by Django 3.0.8 on 2021-03-08 13:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0002_auto_20210308_1305'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnganwadiWorker',
            new_name='AnganwadiWorkers',
        ),
    ]
