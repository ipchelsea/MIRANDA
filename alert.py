from twilio.rest import Client

account_sid = 'AC151263fea7e30db4d04a2a67b1d7fb03'
auth_token = 'b41cdb088b5a1e75a7cf710f990f5c33'

def alert_family():
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="ALERT: Ada Lovelace is being pulled over by Officer Tony Shales of the Houston Police Department at Gulf Freeway, Houston, TX 77017 at 9:13 PM. TAP to call.",
                         from_='+12513060440',
                         to='+14256289296'
                    )

