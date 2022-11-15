import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+15134509904"
myCellPhone = "+16822017628"

textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "Hi there!")

print(textmessage.status)
