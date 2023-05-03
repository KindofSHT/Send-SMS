from twilio.rest import Client

account_sid = 'AC8ea09d3669f4ece1e6e680e76dce24df'
auth_token = '6a1e107325c25e7c7dbbb3fffd77b573'
client = Client(account_sid, auth_token)

for i in range(100):
    message = client.messages.create(
        body='HAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHHHAHAHAHHAHAHA!',
        from_='+13203149868',
        to='+639917712508'
    )

    print(f"SMS number {i+1} sent with SID: {message.sid}")