import os
import httpx

print('Cotação do Dollar\n')

dollar = float(input('Digite um valor em U$: '))


#strings de cada moeda

dol = 'USD'
real = 'BRL'

#utilizando a API para buscar a cotação

cotacao = httpx.get(
    url=f'https://api.exchangerate.host/latest?base={dol}'
).json()

real_data = cotacao['rates']


#calculo da conversão

conversao = dollar * real_data.get(real)


#resultado

print('\nU$' + str(round(dollar, 2)) + ' atualmente equivale a R$' + str(round(conversao, 2)))

os.system("pause")