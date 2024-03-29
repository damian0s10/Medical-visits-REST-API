# Generated by Django 3.1.1 on 2020-11-09 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalClinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.doctor', verbose_name='doctor_visits')),
                ('medical_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.medicalclinic', verbose_name='clinic_visits')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.patient', verbose_name='patient_visits')),
            ],
        ),
    ]
