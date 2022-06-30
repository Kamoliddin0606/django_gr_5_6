from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='catetegory/', null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)

    def __str__(self):
        return self.title

