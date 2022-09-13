idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('Você é menor de idade')
elif idade >= 18 and idade < 65:
    print('Você é adulto')
elif idade >= 65 and idade < 100:
    print('Você está na melhor idade')
elif idade >= 100:
    print('Você é centenário')
