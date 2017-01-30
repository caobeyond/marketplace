from django.db import models
import uuid
from .libs import fields
# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length = 32)
    description = models.CharField(max_length = 128, blank = True, null = True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)
    parent_category = models.ForeignKey('self', null = True, blank=True)
    cover = models.ImageField(upload_to = 'category', blank = True)
    description = models.TextField(blank = True)
    sequence = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    sku = models.CharField(max_length= 128,blank = True, null = True,unique = True)
    slug = models.CharField(max_length=64, blank = True, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    cover = models.ImageField(upload_to = 'product')
    description = models.TextField(blank = True)
    unit = models.ForeignKey(Unit, null = True)
    sequence = models.IntegerField(default = 100)
    status =  models.IntegerField(default=0, choices = (
        (0, 'pending'),
        (1, 'active'),
        (2, 'retired')
    ))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class RelatedProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='related_product')
    related_product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='related_related_product')

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to = 'product_image')

class Client(models.Model):
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length = 200)
    company_name = models.CharField(max_length=200,blank=True)
    company_number = models.CharField(max_length=200, blank=True)
    email =  models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 1, choices =
        (
            ('m','Male'),
            ('f', 'Female'),
            ('*', 'No specified')
        )
    )
    description = models.TextField(blank = True)
    phone_number = models.CharField(max_length = 100)
    alter_phone_number = models.CharField(max_length = 100)
    address =  models.CharField(max_length = 200)
    province = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20, default = "CANADA" )
    profile = models.ImageField(upload_to = "client")
    post_code = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length = 200)
    company_name = models.CharField(max_length=200,blank=True)
    company_number = models.CharField(max_length=200, blank=True)
    email =  models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 1, choices =
        (
            ('m','Male'),
            ('f', 'Female'),
            ('*', 'No specified')
        )
    )
    description = models.TextField(blank = True)
    phone_number = models.CharField(max_length = 100)
    alter_phone_number = models.CharField(max_length = 100)
    address =  models.CharField(max_length = 200)
    province = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20, default = "CANADA" )
    profile = models.ImageField(upload_to = "contractor")
    post_code = models.CharField(max_length = 10)
    score = models.IntegerField(default = 100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length = 64)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_producttype')
    description = models.CharField(max_length=128, blank = True)
    valueType = models.CharField(max_length = 1, choices =
        (
            ('t','Text Field'),
            ('n', 'Numberic Field'),
            ('s', 'Selection Field')
        )
    )
    affect_price = models.BooleanField(default = False)
    type_rule = models.CharField(max_length=128, blank = True) # can be configure for the selection field
    def __str__(self):
        return self.name

class VendorProductProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendor_product_property_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_product_property_product_vendor', null = True, blank = True)
    key = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='vendor_product_property_producttype')
    value_text = models.CharField(max_length=128, blank = True)
    value_number = models.FloatField(blank = True)
    value_select = models.CharField(max_length=8, blank = True)
    price = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    price_rule = models.CharField(max_length=128, blank=True)

class VendorProduct(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_product_vendor')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendor_product_product')
    price = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    price_rule = models.CharField(max_length=128, blank=True)

class Payment(models.Model):
	client = models.ForeignKey(Client, on_delete = models.CASCADE)
	card_number = fields.EncryptedCharField(max_length = 256) #encrypted card number
	card_holder = models.CharField(max_length = 64)
	expired_month =  models.IntegerField()
	expired_year = models.IntegerField()
	security_code = models.CharField(max_length = 10)
	post_code = models.CharField(max_length = 10)
	@property
	def ending_number(self):
		card_number = CIPHER_SUITE.decrypt(str(self.card_number))
		return card_number[-3:]
	@property
	def card_number_decrypted(self):
		card_number = CIPHER_SUITE.decrypt(str(self.card_number))
		return card_number

class Deposit(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE)
	institute_no = models.CharField(max_length = 10)
	branch_no = models.CharField(max_length = 10)
	acct_no = fields.EncryptedCharField(max_length = 64)
	acct_name = models.CharField(max_length = 128)
	@property
	def acct_number(self):
		return CIPHER_SUITE.decrypt(str(self.acct_no))

class ShoppingCart(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete =  models.CASCADE)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 100)
    alter_phone_number = models.CharField(max_length = 100)
    shipping_address =  models.CharField(max_length = 200)
    city = models.CharField(max_length = 20)
    province = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20, default = "CANADA" )
    post_code = models.CharField(max_length = 20)
    comment = models.TextField(blank = True, null = True)
    shipping_fee = models.FloatField(default = 0)
    total_price = models.FloatField(default =  0)
    status = models.IntegerField(choices =
        (
            (0,'Open'),
            (1, 'Pending'),
            (2, 'Processing'),
            (3, 'Cancelled'),
            (4, 'Complete'),
            (5, 'Shipping'),
            (6, 'Closed'),
            (7, 'Unpaid'),
            (8, 'Recommended'),
            (9, 'Declined'),
            (99, 'Error'),
        )
    )
    status_description = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShoppingItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    number = models.IntegerField()
    unit_price = models.FloatField()
