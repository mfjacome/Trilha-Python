n1 = float(input('Informe a primeira nota:'))
n2 = float(input('Informe a primeira nota:'))
n3 = float(input('Informe a primeira nota:'))
n4 = float(input('Informe a primeira nota:'))

media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print('Aprovado!')
elif media >= 4 and media < 7:
    print('Recuperação! ')
else:
    print('Reprovado! ')