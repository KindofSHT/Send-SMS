from twilio.rest import Client

account_sid = 'Your Account SID'
auth_token = 'Your Auth Token'
client = Client(account_sid, auth_token)

for i in range(100):
    message = client.messages.create(
        body='Hello from Twilio!',
        from_='Your Twilio Number',
        to='Your Phone Number'
    )

    print(f"SMS number {i+1} sent with SID: {message.sid}")