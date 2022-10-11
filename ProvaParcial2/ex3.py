#Defina a função quadrados que recebe como argumento um número natural $n$ devolve a 
#lista dos $n$ primeiros quadrados perfeitos.

def quadrados(n):
    return n ** 2

if __name__ == '__main__':
    quadrados(5)
    print(list(map(lambda p : quadrados(p), range(1,6))))
