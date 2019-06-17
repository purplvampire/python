#! python3
# textMyself.py - Defines the textmyself() function that texts a message passed to it as a string.

# Import twilio SID and Auth_token.
twilioID = []
with open('twilioPW.txt', 'r') as f:
    for i in f:
        twilioID.append(i)

# Import twilio client service.
from twilio.rest import Client

account_sid = twilioID[0]
auth_token = twilioID[1]
client = Client(account_sid, auth_token)

def textmyself(message):
    # Send SMS from Twilio Service
    message = client.messages.create(
                        body= message,
                        from_= twilioID[2],
                        to= twilioID[3])
    # Get sending status
    print(message.status)