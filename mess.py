from twilio.rest import Client

account_sid = 'ACa692427848369035b409b363b2f8d938'
auth_token = '6ad0bf1a8c119cb9088e2e88cec9035f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGf065a48a6ee6440caea453956bcd62ec',
    body='Hi, how are you ',
    to='+919100904055'
)

print(message.sid)