
import json
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Greeting

SLACK_API_TOKEN = environ.get('SLACK_API_TOKEN', None)
SLACK_BOT_TOKEN = environ.get('SLACK_BOT_TOKEN', None)
sc = SlackClient(SLACK_API_TOKEN)
bot = SlackClient(SLACK_BOT_TOKEN)

consumer_key = environ.get('consumer_key', None)
consumer_secret = environ.get('consumer_secret', None)
access_token = environ.get('access_token', None)
access_token_secret = environ.get('access_token_secret', None)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

# Create your views here

def get_channel(request):
    channel_event= json.loads(request.body)
    #text_event= json.loads(request.body)
    url_token = channel_event['token']
    if os.environ.get("ver_token") == url_token:
        chal = channel_event['event']['challenge']
        text = channel_event['event']['text']
    else:
        chal = "No challenge key"
        text = "No text found"
    return request

@csrf_exempt
def slack(request):
    request_body = json.loads(request.body)
    url_token = request_body['token']

    if os.environ.get("ver_token") == url_token:
       # chal = request_body['challenge']
        get_channel(request);
    else:
        #chal = "No challenge key"
    return HttpResponse(chal,content_type="text/plain")


