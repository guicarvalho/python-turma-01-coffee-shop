class ProductTemplateView:

    def template_menu(self):
        return """
        Operação
        =============
        1 - Cadastrar
        2 - Listar
        3 - Sair
        : """

    def template_insert(self, instance):
        instance.description = input('Descrição: ')
        instance.price = input('Preço: ')
        instance.stock = input('Estoque: ')

