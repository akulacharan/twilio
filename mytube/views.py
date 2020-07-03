from django.shortcuts import render
from . import models
from twilio.rest import Client





# Create your views here.

def home(request):
    return render(request,'base.html')

def new_search(request,model=None):
    search=request.POST.get('search')
    models.search.objects.create(search=search)

    account_sid = 'AC911bd0d30df0c380d60627a53eb8f52d'
    auth_token = 'f145947a286f3da59346b338dcb29c1f'
    client = Client(account_sid, auth_token)

    message =search
    msg = client.messages.create(from_="+12028318347", body=message, to="+917032172247")
    print(msg.body)

    return render(request,'main/index.html',{'search':search})