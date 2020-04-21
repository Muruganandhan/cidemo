from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def healthchk(request, *args, **kwargs):
    return HttpResponse(status=200)