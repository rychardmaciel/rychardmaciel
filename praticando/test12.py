#by Rychard Maciel 
#Calculando Descontos

produto = float (input ("Qual o preço do produto? R$ "))
desconto = produto - (produto * 5 / 100)
print ("O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}" .format(produto, desconto))