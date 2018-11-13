from django.db import models

from django.core.validators import MinValueValidator


class Product(models.Model):
    description = models.CharField('Descrição', max_length=100)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    stock = models.IntegerField('Estoque', validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Product ({self.description})'
