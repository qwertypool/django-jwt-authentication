from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICE = (
        ('electronics','Electronics'),
        ('food','Food & Beverages'),
        ('accessories','Accessories'),
        ('health','Healthcare')
    )
    product_id = models.IntegerField(unique=True)
    name = models.CharField(max_length = 150,default="")
    category = models.CharField(max_length = 20,choices = CATEGORY_CHOICE)
    price = models.IntegerField(default=0)
    manufacture_date = models.DateField(auto_now=False, auto_now_add=False)
    expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    
    
    

    
    
    