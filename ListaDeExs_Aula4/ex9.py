n = int(input('Insira um valor: '))

f = 0
soma = 1

if n<=0:
    print('A sequencia de fibonacci é: ', f)
else:
    print(f, soma, end=" ")
    for x in range(2,n):
        prox = f + soma
        print(prox, end=" ")
        f = soma
        soma = prox