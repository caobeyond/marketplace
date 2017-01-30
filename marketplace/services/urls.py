from django.conf.urls import url
from . import views
from apps import categories, products,  vendors, orders, carts

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^categories$',categories.list, name = 'categories'),
    url(r'^products$',products.list, name = 'products'),
    url(r'^product/(?P<product_id>[0-9]+)$', products.get_product, name = 'product'),
    url(r'^products/category/(?P<category_id>[0-9]+)$', products.list_by_category, name = 'product_category'),
    url(r'^vendors/product/(?P<product_id>[0-9]+)$',vendors.list_by_product, name = 'vendor_list_by_product'),
    url(r'^orders$', orders.create, name = 'create_order'),
    url(r'^shoppingcart/(?P<cart_id>[0-9]+)$', carts.get_cart, name = 'shopping_cart')
]
