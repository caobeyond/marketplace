import json
from datetime import date

from django.shortcuts import render

from django.http import HttpResponse
from django.middleware import csrf
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.http import JsonResponse

from common.lib.decorators import AuthClientForFunc, AllowMethod, JSONRequest, CurrentUser, Jsonize

from ..json_serializers import *

from store.models import Category, Product

@Jsonize(ProductSerializer, many = True)
def list(request):
    limit = int(request.GET.get('limit','1000'))
    count = int(request.GET.get('count','0'))
    startCount = count * limit
    endCount = (count + 1)* limit
    return Product.objects.filter(status = 1).order_by('sequence', '-updated_at')[startCount:endCount]

@Jsonize(ProductSerializer, many = True)
def list_by_category(request,category_id):
    limit = int(request.GET.get('limit','1000'))
    count = int(request.GET.get('count','0'))
    startCount = count * limit
    endCount = (count + 1)* limit
    #Get the full category list(itself and the children)
    category = Category.objects.get(id=category_id)
    category_list = []
    category_list.append(category)
    __getSubCategories(category_list, category.id)
    return Product.objects.filter(status = 1, category__in=[c.id for c in category_list]).order_by('sequence', '-updated_at')[startCount:endCount]

@Jsonize(ProductSerializer)
def get_product(request, product_id):
    return Product.objects.get(id = product_id)

def __getSubCategories(category_list, parent_id):
    sub_cateogries = Category.objects.filter(parent_category_id = parent_id)
    if sub_cateogries.exists():
        for sub_cateogry in sub_cateogries:
            category_list.append(sub_cateogry)
            __getSubCategories(category_list, sub_cateogry.id)
    else:
        return
