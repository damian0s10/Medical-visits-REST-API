from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class PatientSerializerGET(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['pesel', 'user']


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['pesel', 'user']



class SpecjalizationSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=True)

        

class DoctorSerializerGET(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    specjalizations = SpecjalizationSerializer(read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = ['about_me', 'user','specjalizations', 'doctor_clinic']


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['about_me', 'user','specjalizations']



        
class MedicalClinicSerializerGET(serializers.ModelSerializer):
    doctor = DoctorSerializerGET()

    class Meta:
        model = MedicalClinic
        fields = ['id','city', 'street', 'local', 'doctor']

class MedicalClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalClinic
        fields = ['id','city', 'street', 'local', 'doctor']




class AvailableVisitsSerializerGET(serializers.ModelSerializer):
    doctor = DoctorSerializerGET()
    medical_clinic = MedicalClinicSerializerGET()

    class Meta:
        model = AvailableVisits
        fields = ['id','doctor','medical_clinic','time','date','is_available','doctor']

class AvailableVisitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailableVisits
        fields = ['id','doctor','medical_clinic','time','date','is_available','doctor']


class MedicalVisitSerializerGET(serializers.ModelSerializer):
    doctor = DoctorSerializerGET()
    medical_clinic = MedicalClinicSerializerGET()

    class Meta:
        model = MedicalVisit
        fields = ['id','doctor','patient','medical_clinic','time','date','note','doctor']

class MedicalVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalVisit
        fields = ['id','doctor','patient','medical_clinic','time','date','note','doctor']
