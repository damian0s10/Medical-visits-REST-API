from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from .tasks import send_email_with_reset_password

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    token = reset_password_token.key
    
    user_email = reset_password_token.user.email
    
    send_email_with_reset_password(user_email,token)

    

