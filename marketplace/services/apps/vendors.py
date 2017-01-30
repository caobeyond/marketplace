import json
from datetime import date

from django.shortcuts import render

from django.http import HttpResponse
from django.middleware import csrf
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.http import JsonResponse

from common.lib.decorators import AuthClientForFunc, AllowMethod, JSONRequest, CurrentUser, Jsonize

from ..json_serializers import *

from store.models import *

@Jsonize(VendorProductSerializer, many = True)
def list_by_product(request, product_id):
    return VendorProduct.objects.filter(product_id = product_id)
