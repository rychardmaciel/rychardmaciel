#by Rychard Maciel 
#Programa de Cadastro (Básico)

import os
print ("### System Briquilaus ###")
while True:
    os.system ('cls')
    print ("(0) Sair")
    print ('(1) Cadastro')
    print ('(2) Relatórios')
    print ('(3) Análises')
    op = input ('Opção: ')
    if op == "0": 
        break
    elif op == "1":
        print ('Cadastro Briquilaus ->')
        nome = input ('Nome: ')
        email = input ('E-mail: ')
    elif op == "2":
        print ('Relatório Briquilaus ->')
    elif op == "3":
        print ('Análises Briquilaus ->')
    else:
        print ('Opção inválida.')
        input ()
print ('Acabouuuuu...')