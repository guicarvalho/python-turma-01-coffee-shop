class Product:

    def __init__(self, description, price, stock):
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f'Product ({self.description}, {self.price})'
