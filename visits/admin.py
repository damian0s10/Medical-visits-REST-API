from django.contrib import admin
from .models import *

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'pesel')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)