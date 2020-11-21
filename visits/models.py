from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pesel = models.CharField(max_length=11)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class MedicalClinic(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    local = models.CharField(max_length=10)

class MedicalVisit(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='doctor_visits', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, verbose_name='patient_visits', on_delete=models.CASCADE)
    medical_clinic = models.ForeignKey(MedicalClinic, verbose_name='clinic_visits', on_delete=models.CASCADE) 
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

