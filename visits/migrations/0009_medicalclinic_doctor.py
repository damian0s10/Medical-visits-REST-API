# Generated by Django 3.1.1 on 2020-11-26 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0008_auto_20201126_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalclinic',
            name='doctor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='visits.doctor', verbose_name='doctor_clinic'),
            preserve_default=False,
        ),
    ]
