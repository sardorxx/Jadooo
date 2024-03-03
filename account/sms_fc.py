# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

account_sid = "AC70d4d9e0c21fd59664e50b57b86e225c"
auth_token = "d380dce7ab6a64feb0286f61c7bf2fb0"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+998333037068',
                     to='+998932014605'
                 )

print(message.sid)
