#Calculadora que calcula a raiz de um número 

import os

print('Calculadora de Raízes\n')

#entrada de dados

i = int(input('Digite o índice da raíz: '))

rn = float(input('\nDigite o radicando da raíz: '))


#calculo da raiz

r = pow(rn, (1/float(i)))


#funcao que remove o 0 a esquerda do float

def formatarNumero(num) :
    if (num % 1 == 0) :
        return int(num)   
    else :
        return num  


#saida

if (i == 2) :
    print('\nRaíz Quadrada de ' + str(formatarNumero(rn)) + ' é ' + str(formatarNumero(r)))
elif (i == 3) :
    print('\nRaíz Cúbica de ' + str(formatarNumero(rn)) + ' é ' + str(formatarNumero(r)))
else :
    print('\nRaíz ' + str(i) + '° de ' + str(formatarNumero(rn)) + ' é ' + str(formatarNumero(r)))  

os.system("pause")