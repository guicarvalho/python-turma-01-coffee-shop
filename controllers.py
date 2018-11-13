import csv
import sqlite3

from models import Product
from views import ProductTemplateView


product_view = ProductTemplateView()

conn = sqlite3.connect('coffee_shop.db')
cursor = conn.cursor()


def insert():
    # import pdb; pdb.set_trace()  # < py3.7
    # breakpoint()  # >= py3.7
    product = Product('', 0, 0)
    product_view.template_insert(product)

    product.save(cursor, conn)

    print('Produto cadastrado com sucesso!')


def list_all():
    products = Product.list(cursor)

    if not len(products):
        print('Não existe produto cadastrado!')
    else:
        template = """
        + Descrição: {0}
        + Preço: {1}
        """
        for row in products:
            print(template.format(row[1], row[2]))


def export_csv():
    with open('coffees.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(['ID', 'Descrição', 'Preço', 'Estoque'])
        for row in Product.list(cursor):
            writer.writerow([row[0], row[1], row[2], row[3]])

    print('Registros exportados com sucesso!')


def import_csv():
    with open('/tmp/coffee_shop/coffees.csv') as f:
        count = 0
        reader = csv.reader(f, delimiter=',')

        for (idx, row) in enumerate(reader):
            if idx == 0:
                continue

            product = Product(row[1], row[2], row[3])
            product.save(cursor, conn)
            count += 1

    print('Arquivo importado com sucesso!')
    print(f'Foram criados {count} registros.')


def show_menu():
    op = -1
    while op != 7:
        op = int(input(product_view.template_menu()))

        if op == 1:
            insert()
        elif op == 2:
            list_all()
        elif op == 5:
            export_csv()
        elif op == 6:
            import_csv()

if __name__ == '__main__':
    cursor.execute('CREATE TABLE IF NOT EXISTS product (id integer primary key autoincrement, description text, price real, stock integer)')
    show_menu()
    conn.close()

