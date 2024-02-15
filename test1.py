from twilio.rest import Client

account_sid = 'AC3d0d251daa480d5d088da4c08a7bac56'
auth_token = '52ba17d39b4bc6e13cd69a01cdde7137'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14243532012',
  to='+917032229659',
  body="sollekum"
)

print(message.sid)