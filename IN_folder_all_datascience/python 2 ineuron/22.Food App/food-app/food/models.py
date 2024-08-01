from django.db import models


class Food(models.Model):
    food_item = models.CharField(max_length=200)  # Should be text only
    quantity = models.IntegerField()  # Should be integer only
    calories = models.IntegerField()  # Should be integer only
    # Automatically sets date to current date
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.food_item + " " + str(self.quantity) + ' ' + str(self.calories)
