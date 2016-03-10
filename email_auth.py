from django.contrib.auth.models import User
from django.conf import settings

class EmailAuth(object):
    """authenticate a user with an email and a passowrd
    add EmailAuth to AUTHENTICATION_BACKENDS in the project settings.py
    checkes for DEBUG_ALLOW_NON_UNIQUE_EMAIL, if True will return the first user with email
    Note: by default django does not enforce unique emails.
    To use unique emails add check the email provided in the user registration"""
    
    def get_user(self,user_id):
        
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
                
    def authenticate(self,username,password):
 
        try:
            
            if settings.DEBUG and settings.DEBUG_ALLOW_NON_UNIQUE_EMAIL:
                user = User.objects.filter(email=username).first()
            else:
                user = User.objects.get(email=username)
                
            if user !=None and user.is_active and user.check_password(password):
                return user
            else:
                return None            
                
        except User.DoesNotExist:
            return None
        

            
             
             
        
        
        