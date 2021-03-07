# Generated by Django 3.0.8 on 2021-03-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('Document', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='image_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]
