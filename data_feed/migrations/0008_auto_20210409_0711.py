# Generated by Django 3.0.8 on 2021-04-09 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_feed', '0007_auto_20210331_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinformation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sociodemographicmodel',
            name='guardian_occupation',
            field=models.CharField(blank=True, choices=[('Accountants', 'Accountants'), ('Administrative Assistants', 'Administrative Assistants'), ('Advocates', 'Advocates'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Architects', 'Architects'), ('Assemblers', 'Assemblers'), ('Auditors', 'Auditors'), ('Business Person', 'Business Person'), ('Cleaners', 'Cleaners'), ('College Principals', 'College Principals'), ('Commercial Truck Drivers', 'Commercial Truck Drivers'), ('Cooks', 'Cooks'), ('Craftsmen', 'Craftsmen'), ('Crane Operators', 'Crane Operators'), ('Doctors', 'Doctors'), ('Engineers', 'Engineers'), ('Expert Musicians', 'Expert Musicians'), ('Farmers', 'Farmers'), ('Fishermen', 'Fishermen'), ('Garbage Collector', 'Garbage Collector'), ('General Office Clerks', 'General Office Clerks'), ('Housekeeper/ Housemaid (Hotels/ House)', 'Housekeeper/ Housemaid (Hotels/ House)'), ('Lecturers', 'Lecturers'), ('Mechanist', 'Mechanist'), ('Newspaper Editors', 'Newspaper Editors'), ('Nurse', 'Nurse'), ('Office Assistants', 'Office Assistants'), ('Paramedics', 'Paramedics'), ('Plant And Machine Operators', 'Plant And Machine Operators'), ('Plumbers', 'Plumbers'), ('Police Officers', 'Police Officers'), ('Reading And Emptying Meters', 'Reading And Emptying Meters'), ('Receptionists', 'Receptionists'), ('Retired', 'Retired'), ('Salesman', 'Salesman'), ('Scientists', 'Scientists'), ('Security Guard (Housing Societies/Company/Banks/Land)', 'Security Guard (Housing Societies/Company/Banks/Land)'), ('Senior Administrative Officers', 'Senior Administrative Officers'), ('Software Development', 'Software Development'), ('Soldiers', 'Soldiers'), ('Stocking Vending Machines', 'Stocking Vending Machines'), ('Street Vendor', 'Street Vendor'), ('Sweeper', 'Sweeper'), ('Unemployed', 'Unemployed'), ('OTHERS', 'OTHERS')], max_length=300),
        ),
    ]
