from celery import task
from django.core.mail import send_mail, EmailMessage
from medicalvisits import settings


@task
def send_email_with_reset_password(user_email,token):
    
    subject = 'Password reset'
    message = 'Hi. Here you have a link to change your password, it is available for 24 hours. {}?token={}'.format('www.mywebsite.com/', token)
    
    send_mail(subject,message, settings.EMAIL_HOST , [user_email])