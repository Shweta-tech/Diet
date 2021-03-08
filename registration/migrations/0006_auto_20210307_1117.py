# Generated by Django 3.0.8 on 2021-03-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20210307_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='anemicadolescentgirl',
            name='foodhabits',
            field=models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='anemiclactatingmother',
            name='foodhabits',
            field=models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='anemicpregnantwoman',
            name='foodhabits',
            field=models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='schooladdress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='schoolcontactinformation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='schoolcordinatorincharge',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='schoolname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='uploaded_photo',
            field=models.ImageField(default=False, upload_to='student/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='smchild',
            name='foodhabits',
            field=models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True),
        ),
    ]
