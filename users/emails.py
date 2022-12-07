from django.core.mail import send_mail
from django.conf import settings
import random
import re
import phonenumbers
from .utils import Config
import requests
from .models import User
def send_otp(email):
    subject = "Account Verification Email From JWT App"
    otp = random.randint(1000, 9999)
    message = f"Your OTP is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject,message, email_from,[email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()


conf = Config()



def sender(phone_number):
    otp = random.randint(1000, 9999)
    message = f"Your OTP is {otp}"
    user_obj = User.objects.get(email=phone_number)
    user_obj.otp = otp
    user_obj.save()
    data = {
        
        'messages': [
            {
                'recipient': phone_number,
                'message-id': '{}{}'.format(conf.PREFIX, 1),
                'sms': {
                    'originator': conf.ORIGINATOR,
                    'content': {
                        'text': message
                    }
                }
            }
        ]
    }
    response = requests.post(conf.URL, json=data, headers=conf.HEADER)
    
    return response


def emailcheck(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat,s):
        return True
    else:
        return False

def phonecheck(s):
    if s.isupper() or s.islower():
        return False
    else:
        try:
            my_number = phonenumbers.parse(s)
            result = phonenumbers.is_valid_number(my_number)
        except: 
            result = False
        return result

def phone_or_mail(mail):
    phone_check = phonecheck(mail)
    email_check = emailcheck(mail)
    if phone_check:
        sender(mail)
        return True
    elif email_check:
        send_otp(mail)
        return True
    else:
        return False
