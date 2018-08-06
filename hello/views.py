
import json
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Greeting

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


