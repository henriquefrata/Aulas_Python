class Produto: 
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Pedido:
    def __init__(self, itens, quantidade, pagamento):
        self.itens = itens
        self.quantidade = quantidade
        self.pagamento = pagamento

        if (pagamento == 'dinheiro' or pagamento == 'cartão' or pagamento == 'cheque'):
            pagamento = True
        else:
            pagamento = False

def main():
    produto1 = Produto('alface', 5, 10)
    pedido1 = Pedido(produto1, 3, 'dinheiro')

    print(pedido1.itens)



if __name__ == '__main__':
        main()
  
    
