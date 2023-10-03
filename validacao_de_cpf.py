
#consulta de cpf valido

import os
os.system('clear')

cpf = input("Digite seu CPF: ")
nove_digito = cpf [:9]
dez_digito = cpf [:10]
resultado_dig_1 = 0
resultado_dig_2 = 0
contador_regressivo_1 = 10
contador_regressivo_2 = 11
digito_final = 0 
caracter = cpf [9:11] 



for digito_1 in nove_digito:
    
    resultado_dig_1 += int(digito_1)*contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = resultado_dig_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0 


for digito_2 in dez_digito:
    
   
    resultado_dig_2 += int(digito_2)*contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = resultado_dig_2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0 


digito_final = str(digito_1) + str(digito_2)


if digito_final == caracter:
    print('O CPF informado é VALIDO')
else:
    print('O CPF informado é INVALIDO')