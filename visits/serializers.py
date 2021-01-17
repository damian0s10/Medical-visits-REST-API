from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['pesel', 'user']

class SpecjalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specjalization
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    specjalizations = SpecjalizationSerializer()
    class Meta:
        model = Doctor
        fields = ['about_me', 'user','specjalizations']


class MedicalClinicSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = MedicalClinic
        fields = ['id','city', 'street', 'local', 'doctor']

class AvailableVisitsSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    medical_clinic = MedicalClinicSerializer()

    class Meta:
        model = AvailableVisits
        fields = ['id','doctor','medical_clinic','time','date','is_available','doctor']


class MedicalVisitSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    medical_clinic = MedicalClinicSerializer()

    class Meta:
        model = AvailableVisits
        fields = ['doctor','patient','medical_clinic','time','date','note','doctor']
