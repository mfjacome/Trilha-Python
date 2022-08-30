#Financiamento de imóvel: Programa para aprovar empréstimo bancário para compra de uma casa.

valor_casa = float(input('Qual o valor do imóvel? '))
salario_cliente = float(input('Qual o seu salário mensal? '))
qtd_anos_financiamento = int(input('Quantos anos estima pagar o imóvel? '))

valor_parcela_mensal = float(valor_casa / qtd_anos_financiamento)

pct_salario_30 = int((salario_cliente * 30)/100)
pct_salario_35 = int((salario_cliente * 35)/100)

if valor_parcela_mensal <= pct_salario_30:
    print('Crédito aprovado!')
elif valor_parcela_mensal > pct_salario_30 and valor_parcela_mensal <= pct_salario_35:
    print('Rever a quantidade de anos e o valor do imóvel.')
else:
    print('Crédito reprovado!')

#print(f'O valor da parcela mensal é: {valor_parcela_mensal:.2f}')
#print(f'{pct_salario:.2f}')