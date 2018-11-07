from models import Product
from views import ProductTemplateView


DATABASE = []
product_view = ProductTemplateView()


def insert():
    # import pdb; pdb.set_trace()  # < py3.7
    # breakpoint()  # >= py3.7
    product = Product('', 0, 0)
    product_view.template_insert(product)
    DATABASE.append(product)
    print('Produto cadastrado com sucesso!')


def list_all():
    if not len(DATABASE):
        print('Não existe produto cadastrado!')
    else:
        template = """
        + Descrição: {0}
        + Preço: {1}
        """
        for row in DATABASE:
            print(template.format(row.description, row.price))


def show_menu():
    op = -1
    while op != 3:
        op = int(input(product_view.template_menu()))

        if op == 1:
            insert()
        elif op == 2:
            list_all()


if __name__ == '__main__':
    show_menu()

