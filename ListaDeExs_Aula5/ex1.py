from pickle import FALSE
from tkinter import TRUE


class Produto:
    def __init__(self, nome, preco, Estoque):
        self.nome = nome
        self.preco = preco
        self.Estoque = Estoque
    
    def estoque(self, valor=5):
        estoque = self.Estoque + valor
        return estoque

class Cliente:
    def __init__(self, nome):
        self.nome = nome
    
    def pedido(self, item, quantidade, pagamento):
        return item, quantidade, pagamento

class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Pedido:
    def __init__(self, item, pagamento):
        self.item = item
        self.pagamento = pagamento

    def tp_pagamento(self, pagamento):
        if (pagamento == 'cartão' or 'dinheiro' or 'cheque'):
            pagamento = TRUE
        else:
            pagamento = FALSE






def main():

    produto1 = Produto('Figo',4,10)
    produto2 = Produto('Uva',5,10)
    produto3 = Produto('Maçã',6,10)
    produto4 = Produto('Goiaba',7,10)
    produto5 = Produto('Pessego',8,10)
    produto6 = Produto('Banana',9,10)
    produto7 = Produto('Pera',3,10)

    cliente1 = Cliente('Andre')
    cliente2 = Cliente('Felipe')
    cliente3 = Cliente('Mateus')
    cliente4 = Cliente('Henrique')
    cliente5 = Cliente('Bernardo')

    print(produto1.Estoque)
    print(produto3.nome)

    pedido1 = Pedido(produto2, 'cartão')

    print(pedido1)

    

    
if __name__ == '__main__':
        main()
