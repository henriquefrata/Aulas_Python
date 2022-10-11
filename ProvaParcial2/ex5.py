#Defina a função indices_pares que recebe como argumento uma lista de números inteiros 
#$w$ e devolve a lista dos elementos de $w$ em posições pares.

def indices_pares(n):
    return list(filter(lambda p: n.index(p) % 2 == 0, n))

if __name__ == '__main__':
    print(indices_pares([4,3,7,1,2,9]))
