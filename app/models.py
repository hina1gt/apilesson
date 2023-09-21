from django.db import models

class Cafe(models.Model):

    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')

    def __str__(self):
        return f'{self.name}'
    
class Menu(models.Model):

    name = models.CharField('Name', max_length=256)
    image = models.ImageField('Image')
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    
class Food(models.Model):

    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')
    image = models.ImageField('Image')
    price = models.PositiveIntegerField('Price')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'