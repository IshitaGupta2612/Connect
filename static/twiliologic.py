# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


account_sid = 'AC7c489a8afa6ec4e4ca96f7c2266d927c'
auth_token = 'fa0a9f655db7b8c9c2e8d5b8c40d0064'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='whatsapp:+14155238886',
         to='whatsapp:+917984476345'
     )

print(message.sid)