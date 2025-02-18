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
    
