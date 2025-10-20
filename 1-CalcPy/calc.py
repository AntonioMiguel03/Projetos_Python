#Calculadora Básica utilizando python

import os

x = int(input('Digite um operando: '))

y = int(input('\nDigite outro operando: '))

opr = input('\nEscolha um operador: \n\n+ Adição \n- Subtração' + 
                '\nx Multiplicação \n/ Divisão \nP Potência\n')

match opr:
    case "+":
        print('\n' + str(x) + ' + ' + str(y) + ' = ' + str(x + y))
    case "-":
        print('\n' + str(x) + ' - ' + str(y) + ' = ' + str(x - y))
    case "X":
        print('\n' + str(x) + ' X ' + str(y) + ' = ' + str(x * y))
    case "x":
        print('\n' + str(x) + ' X ' + str(y) + ' = ' + str(x * y))
    case "/":
        print('\n' + str(x) + ' / ' + str(y) + ' = ' + str(x / y))      
    case "P":
        print('\n' + str(x) + ' ^ ' + str(y) + ' = ' + str(pow(x, y)))           
    case "p":
        print('\n' + str(x) + ' ^ ' + str(y) + ' = ' + str(pow(x, y)))
    case _:           
        print('\nValor Inválido!')         

os.system("pause")