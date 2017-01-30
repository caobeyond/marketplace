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

@AllowMethod('POST')
@JSONRequest
def create(request):
    #import pdb;pdb.set_trace()
    print(request.data)
    data = request.data
    client_id = __getAttr(data, 'client', 'id')
    phone_number = __getAttr(data, 'client','shipping', 'phone')
    alter_phone_number = __getAttr(data,'client','shipping','alter_phone')
    shipping_address = __getAttr(data,'client','shipping','address')
    city = __getAttr(data,'client','shipping','city')
    province = __getAttr(data,'client','shipping','province')
    country = __getAttr(data,'client','shipping','country')
    post_code = __getAttr(data,'client','shipping','post_code')
    comment = __getAttr(data, 'comment')
    items = __getAttr(data, 'items')
    client = Client.objects.get(id=client_id)

    vendorItems = {}
    for item in items:
        if item['vendor_id'] not in vendorItems:
            vendorItems[item['vendor_id']] = []
        vendorItems[item['vendor_id']].append(item)
    #create the shoppingcart
    retVal=[]
    for vendor_id in vendorItems:
        product_items = vendorItems[vendor_id]
        vendor = Vendor.objects.get(id=vendor_id)
        shopping_cart = ShoppingCart(
            vendor = vendor,
            client = client,
            phone_number = phone_number,
            alter_phone_number = alter_phone_number,
            shipping_address =  shipping_address,
            city = city,
            province = province,
            country = country,
            post_code = post_code,
            comment = comment,
            status = 0,
            shipping_fee = 0,
            total_price = 0
        )
        shopping_cart.save()
        total_price = 0
        for product_item in product_items:
            product = Product.objects.get(id =  product_item['id'])
            vendor_product = VendorProduct.objects.get(product = product,vendor = vendor)
            price = vendor_product.price
            quantity = product_item["quantity"]
            shopping_item = ShoppingItem(
                shopping_cart = shopping_cart,
                product = product,
                number = quantity,
                unit_price = price
            )
            total_price = total_price + quantity * price
            shopping_item.save()
        shopping_cart.total_price = total_price
        shopping_cart.save()
        retVal.append(shopping_cart.id)
    return JsonResponse({'success' : True, 'shopping_carts': retVal},safe = False)

def __getAttr(data, *args):
    ret = data
    for arg in args:
        if arg in ret:
            ret = ret[arg]
        else:
            return None
    return ret
