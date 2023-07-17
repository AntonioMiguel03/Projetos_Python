#Veja como fica o seu nome em binário

import os

nome = input('Digite o seu nome: ')

bin = ' '.join(f"{ord(i):08b}" for i in nome)

print('\nSeu nome em binário: \n\n' + str(bin))


os.system("pause")