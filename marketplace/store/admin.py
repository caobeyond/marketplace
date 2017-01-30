from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s"  height="240"/></a> %s ' % \
                          (image_url, image_url, file_name, _('')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class ImageWidgetAdmin(admin.ModelAdmin):
    image_fields = []

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.image_fields:
            request = kwargs.pop("request", None)
            #kwargs['widget'] = AdminImageWidget
            return db_field.formfield(widget=AdminImageWidget)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class CategoryAdmin(ImageWidgetAdmin):
    list_display =  ('name','parent_category')
    image_fields = ['cover']

admin.site.register(Category, CategoryAdmin)

class ProductTypeInline(admin.TabularInline):
    model= ProductType
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class VendorProductPropertyInline(admin.TabularInline):
    model = VendorProductProperty
    extra = 1

class ProductAdmin(ImageWidgetAdmin):
    list_display=('name','category')
    image_fields = ['cover']
    inlines = [ProductImageInline, ProductTypeInline,VendorProductPropertyInline]

admin.site.register(Product, ProductAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Unit, UnitAdmin)



class VendorProductInline(admin.TabularInline):
    model =  VendorProduct
    extra = 1
class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1
class DepositInline(admin.TabularInline):
    model = Deposit
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number')
    inlines = [PaymentInline]
admin.site.register(Client, ClientAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number','company_name')
    inlines = [DepositInline,VendorProductInline]
admin.site.register(Vendor, VendorAdmin)

class ShoppingItemInline(admin.TabularInline):
    model = ShoppingItem
    extra = 1
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('client','vendor','total_price','shipping_fee','status','created_at','updated_at')
    inlines = [ShoppingItemInline]
admin.site.register(ShoppingCart, ShoppingCartAdmin)
