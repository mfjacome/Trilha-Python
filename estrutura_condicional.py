idade = int(input('Qual sua idade?'))

#Estrutura Condicional Simples: Testa apenas a condição verdadeira.
if idade > 17:
    print('Já tem maior idade.')

#Estrutura Condicional Composta: Testa a condição verdadeira, caso seja falsa exibe o resultado da outra condição.
if idade >= 18: #Se a condição for verdadeira será executada.
    print('Já tem maior idade.')#True
else: #Se a condição for falsa será executada.
    print('Menor de idade.')#False