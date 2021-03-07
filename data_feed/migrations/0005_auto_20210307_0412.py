# Generated by Django 3.1.7 on 2021-03-07 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_feed', '0004_auto_20210303_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdolescentAnemicGirl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(max_length=50)),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.IntegerField()),
                ('hemoglobinvalue', models.IntegerField()),
                ('hemoglobindate', models.DateField(blank=True, default=datetime.datetime.now)),
                ('food', models.CharField(max_length=50)),
                ('complication', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('medication', models.CharField(max_length=50)),
                ('health', models.CharField(max_length=50)),
                ('medical', models.CharField(max_length=50)),
                ('uploaded_file', models.FileField(upload_to='adolescentgirldocuments/%Y/%m/%d')),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AnganwadiWorkerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(default=datetime.datetime.now)),
                ('age', models.CharField(max_length=6)),
                ('age_in_months', models.CharField(max_length=6)),
                ('age_in_days', models.CharField(max_length=6)),
                ('contact', models.CharField(max_length=10)),
                ('personaladdress', models.CharField(max_length=200)),
                ('uploaded_image', models.ImageField(upload_to='anganwadiworkerid/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='MukhyaSevikaProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('dob', models.DateField(blank=True, default=datetime.datetime.now)),
                ('age', models.CharField(default=0, max_length=6, null=True)),
                ('age_in_months', models.CharField(default=0, max_length=6, null=True)),
                ('age_in_days', models.CharField(default=0, max_length=6, null=True)),
                ('personaladdress', models.CharField(max_length=200, null=True)),
                ('uploaded_image', models.ImageField(upload_to='mukhyasevikaid/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='PregnantWoman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(max_length=50)),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.IntegerField()),
                ('hemoglobinvalue', models.IntegerField()),
                ('hemoglobindate', models.DateField(blank=True, default=datetime.datetime.now)),
                ('food', models.CharField(blank=True, max_length=50)),
                ('complication', models.CharField(max_length=50)),
                ('medication', models.CharField(max_length=50)),
                ('health', models.CharField(blank=True, max_length=50)),
                ('medical', models.CharField(max_length=50)),
                ('uploaded_file', models.FileField(upload_to='pregnantwomandocuments/%Y/%m/%d')),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SMChildDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(max_length=50)),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.IntegerField()),
                ('hemoglobinvalue', models.IntegerField()),
                ('hemoglobindate', models.DateField(blank=True, default=datetime.datetime.now)),
                ('food', models.CharField(blank=True, max_length=50)),
                ('complication', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=50)),
                ('medication', models.CharField(max_length=50)),
                ('health', models.CharField(blank=True, max_length=50)),
                ('medical', models.CharField(max_length=50)),
                ('uploaded_file', models.FileField(upload_to='smchilddocuments/%Y/%m/%d')),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SMChildParentsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mothername', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('motherage', models.IntegerField()),
                ('fatherage', models.IntegerField()),
                ('fatheroccupation', models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=100)),
                ('education', models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=50, null=True)),
                ('monthlyincome', models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='AdolescentGirlsModel',
        ),
    ]
