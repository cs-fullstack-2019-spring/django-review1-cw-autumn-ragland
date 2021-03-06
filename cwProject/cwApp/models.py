from django.db import models


# Cocktail models added to in admin
class Cocktail(models.Model):
    name = models.CharField(max_length=200, default='')
    alcoholPercentage = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    servingGlass = models.IntegerField(default=0)

    def __str__(self):
        return self.name
