# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Import twilio SID and Auth_token
twilioID = []
with open('twilioPW.txt', 'r') as f:
    for i in f:
        twilioID.append(i)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = twilioID[0]
auth_token = twilioID[1]
client = Client(account_sid, auth_token)

# Send SMS from Twilio Service
message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_= twilioID[2],
                     to= twilioID[3])

# Get sending status
print(message.status)
