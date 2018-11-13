class ProductTemplateView:

    def template_menu(self):
        return """
        Operação
        =============
        1 - Cadastrar
        2 - Listar
        3 - Atualizar
        4 - Excluir
        5 - Exportar (CSV)
        6 - Importar (CSV)
        7 - Sair
        : """

    def template_insert(self, instance):
        instance.description = input('Descrição: ')
        instance.price = float(input('Preço: '))
        instance.stock = int(input('Estoque: '))

