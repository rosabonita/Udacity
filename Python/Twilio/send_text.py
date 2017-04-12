from twilio.rest import TwilioRestClient

account_sid = "AC2869aae1e8eeafed0f85028c97bc0bdd" # Your Account SID from www.twilio.com/console
auth_token  = "ba8b554ecb6f24ebfc5b227b1e987855"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hi jerk. Msg me if you get this please",
    to="+18435018139",    # Replace with your phone number
    from_="+19402572238") # Replace with your Twilio number

print(message.sid)
