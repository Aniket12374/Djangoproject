from django.contrib import admin
from .models import Product
from .models import Customer
from .models import Cart
from .models import Cartitem
from .models import Order
from .models import OrderItem







class ProductAdmin(admin.ModelAdmin):
       list_display = ('name','desc','color','price','is_active','is_deleted')    
       search_fields = ('name',)
 
class CustomerAdmin(admin.ModelAdmin):
       list_display =  ('name' , 'phone' , 'email', 'age' )
       search_fields = ('phone',) 

class CartAdmin(admin.ModelAdmin):
       list_display =  ('total_price' , 'customer','id')
       search_fields = ('customer',) 

class CartitemAdmin(admin.ModelAdmin):
       list_display =  ('total_quantity','category','product','cart','id') 
       search_fields = ('category',) 

class OrderAdmin(admin.ModelAdmin):
       list_display = ('pricing','customer')
       search_fields = ('customer',)

class  OrderItemAdmin(admin.ModelAdmin):       
       list_display = ('deleivery','order','product','category')
       search_fields = ('product',)







admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Cartitem,CartitemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)





