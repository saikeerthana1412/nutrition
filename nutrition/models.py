from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    nutrients = models.ManyToManyField('Nutrient', through='FoodItemNutrient')

    def _str_(self):
        return self.name

class Nutrient(models.Model):
    name = models.CharField(max_length=100)
    daily_requirement = models.DecimalField(max_digits=8, decimal_places=2)

    def _str_(self):
        return self.name

class FoodItemNutrient(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)

    def _str_(self):
        return {self.food_item.name} - {self.nutrient.name}