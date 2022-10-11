#Defina a função fibonacci que recebe como argumento um número natural $n$ e devolve o 
#$n$-ésimo número da sucessão de Fibonacci. Recorde que a sucessão dos números de 
#Fibonacci é definida recursivamente como se segue:

def fibonacci(n, x = 0, y = 1):
    if n == 0: 
        return x
    else: 
        return fibonacci(n-1, y, x + y)

if __name__ == '__main__':
    print(fibonacci(8))
