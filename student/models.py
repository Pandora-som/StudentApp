from django.db import models

class Groups(models.Model):
    name_group = models.CharField(max_length=20)

    def __str__(self):
        return self.name_group
    
class Students(models.Model):
    number_group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    thirdname = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name}"

