from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'AC5abae1dc9c733998e76bd36c3cbd5005'
auth_token = '1cbbac6958d5059a6e3f7a24fcd65c79'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number
twilio_phone_number = '+18777804236'

# The recipient's phone number
to_phone_number = 'recipient_phone_number'

# Your message
message_body = "Hello, this is a test message from your Python script!"

# Send the message
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=to_phone_number
)

print(f"Message sent with SID: {message.sid}")
