from rest_framework.permissions import BasePermission
from .models import *

class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.id == view.kwargs['pk']

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
                return True
        else:
            return Doctor.objects.get(pk=request.user.id)

class IsOwnerClinic(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            clinic = MedicalClinic.objects.get(pk=view.kwargs['pk'])
            print(clinic.doctor.user.id)
            print(request.user.id )
            return request.user.id == clinic.doctor.user.id

class IsDoctorVisit(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
                return True
        else:
            visit = AvailableVisits.objects.get(pk=view.kwargs['pk'])
            
            return visit.doctor.user.id == request.user.id

            

class IsSpecificDoctor(BasePermission):
    def has_permission(self, request, view):
        return view.kwargs['doctor'] == request.user.id

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_patient


class IsDoctorOrPatient(BasePermission):
    def has_permission(self, request, view):
        visit = MedicalVisit.objects.get(pk=view.kwargs['pk'])
        if request.method == 'GET':
            return visit.doctor.user.id == request.user.id or visit.patient.user.id == request.user.id
        elif request.method == 'PUT':
            return visit.doctor.user.id == request.user.id
        return False
