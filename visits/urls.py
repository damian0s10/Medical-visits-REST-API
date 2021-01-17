from django.urls import path, include
from .api import *
from rest_framework.routers import DefaultRouter

app_name = 'visits'

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('doctors', DoctorListView.as_view()),
     path('doctors/<int:pk>/', DoctorDetail.as_view()),

     path('medicalclinics', MedicalClinicListView.as_view()),
     path('medicalclinics/<int:pk>/', MedicalClinicDetail.as_view()),

     path('availablevisits', AvailableVisitsListView.as_view()),
     path('availablevisits/<int:pk>/', AvailableVisitsDetail.as_view()),

     path('availablevisits/<int:doctor>/<int:clinic>/', AvailableDoctorVisits.as_view()),

     path('create', CreateMedicalVisit.as_view()),

     path('medicalvisits', MedicalVisitsListView.as_view()),
     path('medicalvisits/<int:pk>/', MedicalVisitsDetail.as_view()),
]