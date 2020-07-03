from django.shortcuts import render
import requests
import json
# Create your views here.


def signup(request):
    return render(request, 'login.html')


def submitUser(request):
    email = request.GET['email']
    password = request.GET['psw']
    name = request.GET['username']
    print(email, password, name, "welcome")

    url = "127.0.0.1:8000/apiv2/login/"

    payload = {"email":email, "password":password, "name":name}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    return render(request, 'temp.html', {'data':data })