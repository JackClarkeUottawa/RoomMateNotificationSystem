import twilio

def setup():
    from twilio.rest import Client

    account_sid = "ACa971456efc536e1f853090003309c916"
    auth_token = "ba7834b48e0835fb81a4f74d56bd1340"
    client = Client(account_sid, auth_token)
    return client
def send_message(bod):
    message = client.messages \
        .create(
        body=bod,
        from_='+14436711087',
        to='+1***REMOVED***'
    )

client = setup()
send_message(input("Please type message: "))
