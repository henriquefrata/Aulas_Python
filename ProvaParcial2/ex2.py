# Defina a função soma_nat que recebe como argumento um número natural $n$ e devolve 
#a soma de todos os números naturais até $n$.

def soma_nat(n):
    return n+(soma_nat(n-1) if (n-1) > 1 else 1)


if __name__ == '__main__':
    print(soma_nat(10))
