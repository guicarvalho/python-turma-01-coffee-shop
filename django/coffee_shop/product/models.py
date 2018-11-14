from django.db import models

from django.core.validators import MinValueValidator


class Product(models.Model):
    description = models.CharField('Descrição', max_length=100)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    stock = models.IntegerField('Estoque', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'Produto ({self.description})'
