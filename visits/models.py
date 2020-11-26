from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    class Meta(object):
        unique_together = ('email',)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pesel = models.CharField(max_length=11)



class Specjalization(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    about_me = models.TextField()
    specjalizations = models.ManyToManyField(Specjalization)
    



class MedicalClinic(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    local = models.CharField(max_length=10)
    doctor = models.ForeignKey(Doctor, verbose_name='doctor_clinic', on_delete=models.CASCADE)

    class Meta:
        ordering = ['city']

    def __str__(self):
        return self.city +", "+ self.street + " " + self.local


class MedicalVisit(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='doctor_visits', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, verbose_name='patient_visits', on_delete=models.CASCADE)
    medical_clinic = models.ForeignKey(MedicalClinic, verbose_name='clinic_visits', on_delete=models.CASCADE) 
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['date']