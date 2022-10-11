#Conversor de moedas
#cotação em 07/10/2022#

n = float (input ("Quanto dinheiro você tem na carteira? R$ "))
dólar = n / 5.21
Euro = n / 5.08
print ("Com R$ {:.2f} você pode comprar US$ {:.2f}" .format(n, dólar))
print ("Com R$ {:.2f} você pode comprar EUR {:.2f}" .format(n, Euro))