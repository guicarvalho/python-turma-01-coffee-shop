class Product:

    def __init__(self, description, price, stock):
        self.description = description
        self.price = price
        self.stock = stock

    def save(self, cursor, conn):
        cursor.execute('INSERT INTO product (description, price, stock) VALUES (?,?,?)', (self.description, self.price, self.stock))
        conn.commit()

    @staticmethod
    def list(cursor):
        cursor.execute('SELECT * FROM product ORDER BY price')
        return cursor.fetchall()

    def __repr__(self):
        return f'Product ({self.description}, {self.price}, {self.stock})'
