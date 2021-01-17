# Generated by Django 3.1.1 on 2021-01-04 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0009_medicalclinic_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalvisit',
            name='note',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AvailableVisits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('is_available', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.doctor', verbose_name='doctor_visits')),
                ('medical_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.medicalclinic', verbose_name='clinic_visits')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
