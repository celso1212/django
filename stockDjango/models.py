from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    cod = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    qtd = models.IntegerField()
    discount = models.IntegerField()
    created_at = models.DateField()
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name