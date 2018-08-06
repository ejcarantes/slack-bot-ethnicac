import json
import os
from os import environ

from django.http import HttpResponse
from slackclient import SlackClient
from django.views.decorators.csrf import csrf_exempt
from tweepy import OAuthHandler, API

SLACK_API_TOKEN = environ.get('oAuth_token', None)
SLACK_BOT_TOKEN = environ.get('bot_auth_token', None)
slackC = SlackClient(SLACK_API_TOKEN)
slackBot = SlackClient(SLACK_BOT_TOKEN)

def twittertrends():
    consumer_key = environ.get('consumer_key', None)
    consumer_secret = environ.get('consumer_secret', None)
    access_token = environ.get('access_token', None)
    access_token_secret = environ.get('access_token_secret', None)

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)

    WOE_ID = 1
    trending = api.trends_place(WOE_ID)
    trending = json.loads(json.dumps(trending, indent=1))
    trend_list = []
    for trend in trending[0]["trends"]:
        trend_list.append((trend["name"]))

    trend_list = ', \n'.join(trend_list[:10])

    return trend_list

# Create your views here
def get_channel(request):
    channel_event = json.loads(request.body)
    #text_event= json.loads(request.body)
    chal = channel_event['event']['channel']
    text = channel_event['event']['text']
    if "trending" in text or "twitter" in text:
        slackC.api_call(
            "chat.postMessage",
            channel=chal,
            text=twittertrends(),
            icon_emoji=':robot_face:'
        )
    else:
        slackC.api_call(
            "chat.postMessage",
            channel=chal,
            text="No text found",
            icon_emoji=':robot_face:'
        )
    return request

@csrf_exempt
def slack(request):
    request_body = json.loads(request.body)
    url_token = request_body['token']

    if os.environ.get("ver_token") == url_token:
       # chal = request_body['challenge']
        get_channel(request)
    else:
        print("no token")
        #chal = "No challenge key"
    return HttpResponse(request)
    # return request


