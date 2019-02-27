import os 
import bottle

from bottle import route, run, post, Response
from twilio import twiml
from twilio.rest import TwilioRestClient

app = bottle.default_app()
# plug in account SID and auth token here if they are not already exposed as 
# enviornment variables
twilio_client = TwilioRestClient()

TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', '+12025551234')
NGROK_BASE_URL = os.environ.get('NGROK_BASE_URL', 'https://c6c6d4e8.ngrok.io')

@route('/')
def index():
	"""
	Return a standard text response to show the app is up and running.
	"""
	return Response("Bottle app running!")

if __name__ == '__main__':
	run(host='127.0.0.1', port=8000, debug=False, reloader=True)