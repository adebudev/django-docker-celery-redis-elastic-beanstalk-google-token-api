from django.http import HttpResponse
from django.shortcuts import render
from apps.users.tasks import hello_
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello(request):
    #print(request)
    result = hello_.delay('esteban')
    print(result)
    return Response({'data':'done!'})