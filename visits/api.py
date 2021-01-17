from .models import *
from rest_framework import viewsets
from .serializers import *
from .permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, BasePermission
from datetime import datetime
from django.db.models import Q

class PatientViewSet(viewsets.ModelViewSet):

    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DoctorListView(APIView):
    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class DoctorDetail(APIView):
    permission_classes = (IsOwner,)

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        
        doctor = self.get_object(pk)
        print(doctor.user.id)
        print(request.data)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Medical clinic

class MedicalClinicListView(APIView):
    """
    List all MedicalClinic, or create a new.
    """
    permission_classes = (IsDoctor,)

    def get(self, request, format=None):
        medicalClinic = MedicalClinic.objects.all()
        serializer = MedicalClinicSerializerGET(medicalClinic, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.data['doctor'] == request.user.id:
            serializer = MedicalClinicSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)



class MedicalClinicDetail(APIView):
    """
    Retrieve, update or delete.
    """
    permission_classes = (IsOwnerClinic,)

    def get_object(self, pk):
        try:
            return MedicalClinic.objects.get(pk=pk)
        except MedicalClinic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        medicalclinic = self.get_object(pk)
        serializer = MedicalClinicSerializerGET(medicalclinic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        medicalclinic = self.get_object(pk)
        serializer = MedicalClinicSerializer(medicalclinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        medicalclinic = self.get_object(pk)
        medicalclinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# AvailableVisits


class AvailableVisitsListView(APIView):
    permission_classes = (IsDoctor,)

    def get(self, request, format=None):
        now = datetime.now()
        visits = AvailableVisits.objects.filter(Q(date=now.date(),time__gte=now.time())|Q(date__gt=now.date()))
        serializer = AvailableVisitsSerializerGET(visits, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        if request.data['doctor'] == request.user.id:
            serializer = AvailableVisitsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

class AvailableVisitsDetail(APIView):
    permission_classes = (IsDoctorVisit,)
    def get_object(self, pk):
        try:
            return AvailableVisits.objects.get(pk=pk)
        except AvailableVisits.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        visits = self.get_object(pk)
        serializer = AvailableVisitsSerializerGET(visits)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        visits = self.get_object(pk)
        serializer = AvailableVisitsSerializer(visits, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        visits = self.get_object(pk)
        visits.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AvailableDoctorVisits(APIView):
    permission_classes = (IsSpecificDoctor,)

    def get_object(self, doctor, clinic):
        try:
            return AvailableVisits.objects.all().filter(doctor=doctor).filter(medical_clinic=clinic)
        except AvailableVisits.DoesNotExist:
            raise Http404

    def get(self, request, doctor, clinic, format=None):
        visits = self.get_object(doctor,clinic)
        serializer = AvailableVisitsSerializer(visits, many=True)
        return Response(serializer.data)


# Medical visits

class CreateMedicalVisit(APIView):
    permission_classes = (IsPatient,)

    def get_object(self, pk):
        try:
            return AvailableVisits.objects.get(pk=pk)
        except AvailableVisits.DoesNotExist:
            raise Http404
    
    def post(self, request, format=None):

        available_visit = self.get_object(request.data.get("id"))
        
        if available_visit.is_available:
            medical_visit = MedicalVisit(
                doctor=available_visit.doctor,
                patient=request.user.patient,
                medical_clinic=available_visit.medical_clinic,
                time=available_visit.time,
                date=available_visit.date
            )
            medical_visit.save()
            available_visit.is_available = False
            available_visit.save()

            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MedicalVisitsListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):

        if request.user.is_patient:
            visits = MedicalVisit.objects.filter(patient=request.user.id)
        elif request.user.is_doctor:
            visits = MedicalVisit.objects.filter(doctor=request.user.id)

        serializer = MedicalVisitSerializerGET(visits, many=True)
        return Response(serializer.data)
        
       
    

class MedicalVisitsDetail(APIView):
    permission_classes = (IsDoctorOrPatient,)

    def get_object(self, pk):
        try:
            return MedicalVisit.objects.get(pk=pk)
        except MedicalVisit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        visits = self.get_object(pk)
        serializer = MedicalVisitSerializerGET(visits)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        visit = self.get_object(pk)
        if request.data['doctor'] == visit.doctor.user.id and request.data['patient'] == visit.patient.user.id and request.data['medical_clinic'] == visit.medical_clinic.id:
            serializer = MedicalVisitSerializer(visit, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
         



    
