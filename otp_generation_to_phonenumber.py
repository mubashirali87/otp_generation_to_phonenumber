import random
import string
import smtplib

def generate_otp(length=6):
    otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return otp

def send_sms(otp, to_number):
    message = f"Your OTP is: {otp}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("sender_email_address", "sender_email_password")
    server.sendmail("sender_email_address", to_number, message)
    server.quit()

def send_otp(to_number):
    otp = generate_otp()
    send_sms(otp, to_number)
    return otp

to_number = "recipient_phone_number@service_provider.com"
otp = send_otp(to_number)
print("OTP sent to", to_number)
