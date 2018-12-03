from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    parent =models.ForeignKey('self', null=True, blank=True, related_name='sub_categories', on_delete=models.PROTECT)
    
    def __str__(self):
        if self.parent:
            return "{0} {1}".format(self.name, self.parent)
        else:
            return self.name
        

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    brand = models.CharField(max_length=50, default='')
    sku = models.CharField(max_length=50, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    size = models.IntegerField(default=6)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name