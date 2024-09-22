from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

def account(request):
    return JsonResponse("hello world",safe=False)


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username = data['username'], password= data['password'])
            user.save()
            token = Token.objects.create(user = user)
            return JsonResponse({'token':str(token)},status=201)
        except:
            return JsonResponse({'error':'Username already taken, please take another name'},status=400)

@csrf_exempt
def login(request):
    pass
