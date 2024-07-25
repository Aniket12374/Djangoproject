from django.db import models
from django.contrib.auth.models import User






class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50,blank=True,null=True)
    age = models.CharField(max_length=10,blank=True,null=True ) 


    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50) 
    desc = models.CharField(max_length=50,blank=True,null=True) 
    color = models.CharField(max_length=50 ,blank=True,null=True) 
    price = models.CharField(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)




    def __str__(self):
        return str(self.name)



class Cart(models.Model):
    
    total_price= models.CharField(max_length=50,blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)

    
    def __str__(self):
         return f'{str(self.customer)}- {str(self.customer.id)}-'   


    
class Cartitem(models.Model):
    total_quantity= models.CharField(max_length=50,blank=True,null=True) 
    category = models.CharField(max_length=50,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True)

    
    def __str__(self):

        return str(self.id)

class Order(models.Model):
    pricing= models.CharField(max_length=50,blank=True,null=True) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):

        return str(self.customer)

class OrderItem(models.Model):
    deleivery = models.CharField(max_length= 10,blank = True,null=True)
    order = models.ForeignKey(Order,max_length=20,on_delete=models.CASCADE,blank=True,null=True)
    product =models.ForeignKey(Product,max_length=50,on_delete=models.CASCADE,blank=True,null=True)
    category = models.CharField(max_length=30,blank= True,null=True)    


     
    


 
