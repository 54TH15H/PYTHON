# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import string
import random

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC0715306896647ab99fb0f71c1c960184"
auth_token = "a6a8b8e6ba9561fca6321ab7fbcb548c"
client = Client(account_sid, auth_token)

otp = ''
rand = string.digits + string.ascii_letters
for i in range(6):
    otp += random.choice(rand)

message = client.messages \
                .create(
                     body="\nLibrary Management System \nOTP : "+otp,
                     from_='+13513005666',
                     to='+917036543630'
                 )

print(message.sid)
print(otp)
