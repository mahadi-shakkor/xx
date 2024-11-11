from django.db import models

class Student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)


    # def __str__(self) -> str:
    #     return self.car_name
    
    
from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/')
    
    def __str__(self):
        return self.recipe_name
