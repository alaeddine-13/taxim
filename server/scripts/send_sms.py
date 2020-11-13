import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_SECRET']
client = Client(account_sid, auth_token)
 
message = client.messages.create( 
                              from_='+18555501648',  
                              body='First sms taxim',      
                              to='+21699739801' 
                          ) 


print(message.sid)