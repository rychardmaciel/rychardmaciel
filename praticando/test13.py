#by Rychard Maciel 
#Reajuste Salarial

salario = float (input("Qual é o salário do funcionário? R$ "))
aumento = salario + (salario * 15 /100)
print ("Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}" .format(salario, aumento))
