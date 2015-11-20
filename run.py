# run.py
from batch_sms import BatchSMS
from batch_sms import AssociatedBatchSender
from batch_sms import TwilioSender
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

sender = TwilioSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
batch_sender = AssociatedBatchSender(sender)
client = BatchSMS('test.db', batch_sender, auto_associate=True)

client.add_from_number('+17084983870')
client.add_from_number('+17036216924')
client.add_from_number('+17034571909')
client.add_from_number('+17032935994')

# sub_id = client.create_subscription_list('Hackers')

subs = ['Hackers']
# client.add_to_number('+16096479885', subs=subs)

def callback(payload):
    print payload

def onfail(payload):
    print 'Failed'
    print payload

text = 'Hello from Wildhacks again!'

client.send_to_subscription(subs[0], text, callback=callback)
