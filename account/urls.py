from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi, ChangePasswordView



urlpatterns = [
      path('register', RegisterApi.as_view()),
      path('change-password', ChangePasswordView.as_view(), name='change-password'),
      path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]