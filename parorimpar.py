numeral = int(input('Par ou ímpar? '))
resto = numeral % 2

if resto == 0: 
    print('Número par')
else:
    print('Número ímpar')