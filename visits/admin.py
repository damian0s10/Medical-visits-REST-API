from django.contrib import admin
from .models import *

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'pesel')



@admin.register(Specjalization)
class SpecjalizationAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SpecjalizationInline(admin.TabularInline):
    model = Doctor.specjalizations.through


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user','about_me')
    inlines = (SpecjalizationInline,)


class PatientInline(admin.StackedInline):
    model = Patient

class DoctorInline(admin.StackedInline):
    model = Doctor


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','is_patient',)
    inlines = (PatientInline, DoctorInline)
    list_filter = ('is_patient','is_doctor')


@admin.register(MedicalClinic)
class MedicalClinicAdmin(admin.ModelAdmin):
    pass

@admin.register(MedicalVisit)
class MedicalVisitAdmin(admin.ModelAdmin):
    pass

@admin.register(AvailableVisits)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'medical_clinic', 'time', 'date', 'is_available')
