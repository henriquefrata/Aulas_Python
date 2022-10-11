#Defina a função quadrados_inv que recebe como argumento um número natural $n$ 
#devolve a lista dos $n$ primeiros quadrados perfeitos, por ordem decrescente.

def quadrados_inv(n):
    return n ** 2

if __name__ == '__main__':
    quadrados_inv(5)
    print(list(reversed(list(map(lambda p : quadrados_inv(p), range(1,6))))))