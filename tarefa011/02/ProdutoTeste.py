class Produto:
    def __init__(self, nomeloja, preco):
        self.nomeloja = nomeloja
        self.preco = preco
        self.descricao = "Produto de informática"

    def get_nomeloja(self):
        return self.nomeloja

    def set_nomeloja(self, nomeloja):
        self.nomeloja = nomeloja

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_descricao(self):
        return self.descricao


class Mouse(Produto):
    def __init__(self, nomeloja, preco, tipo):
        super().__init__(nomeloja, preco)
        self.tipo = tipo

    def get_descricao(self):
        return super().get_descricao() + f", Tipo: {self.tipo}"


class Livro(Produto):
    def __init__(self, nomeloja, preco, autor):
        super().__init__(nomeloja, preco)
        self.autor = autor

    def get_descricao(self):
        return super().get_descricao() + f", Autor: {self.autor}"


class ProdutoTeste:
    def __init__(self):
        self.carrinho = []

    def adicionar_produto(self, produto):
        self.carrinho.append(produto)

    def exibir_descricoes(self):
        for produto in self.carrinho:
            print(produto.get_descricao())


# Teste das classes
produto_teste = ProdutoTeste()

produto1 = Mouse("Loja A", 50.0, "Mouse ótico, Saída USB. 1.600 dpi")
produto2 = Livro("Loja B", 100.0, "Autor X")
produto3 = Mouse("Loja C", 30.0, "Mouse sem fio, Bluetooth")

produto_teste.adicionar_produto(produto1)
produto_teste.adicionar_produto(produto2)
produto_teste.adicionar_produto(produto3)

produto_teste.exibir_descricoes()
