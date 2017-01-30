import json
from datetime import date

from django.shortcuts import render

from django.http import HttpResponse
from django.middleware import csrf
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.http import JsonResponse


def index(request):
    return JsonResponse({'token' : csrf.get_token(request)})
