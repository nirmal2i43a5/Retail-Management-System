from django.db import models

# Create your models here.



class Product(models.Model):
    
    category=(
                 ('indoor service','indoor service'),
                 ('outdoor service','outdoor service')
              )
    name=models.CharField(max_length=50,null=True)
    price=models.CharField(max_length=50,null=True)
    category=models.CharField(max_length=200,null=True,choices=category)
    description=models.CharField(max_length=50,null=True)
    created_at=models.DateField(auto_now=True,null=True)


        
    def __str__(self):
        return self.name


