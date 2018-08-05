
import json
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

@csrf_exempt
def slack(request):
    request_body = json.loads(request.body)
    url_token = request_body['token']

    if os.environ.get("ver_token") == url_token:
        chal = request_body['challenge']
    else:
        chal = "No challenge"
    print (chal)
    return ""


