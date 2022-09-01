#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print("Salve, te falo qual ta mais barato")
print("O Leite Tirol")
print("O leite Ninho")
print("O leite de Boi")
print("Me de o valor dos leite")
tirol = input("Me passa o valor do Tirol")
ninho = input("Me passa o valor do Ninho")
boi = input("Me passa o valor do de Boi")
barato = tirol

if ninho < tirol and ninho < boi:
    barato = ninho
    print("O ninho ta barateza, só R$",barato)
if boi < ninho and boi < tirol:
    barato = boi
    print("Vai no de boi irmão, só R$",barato)
if tirol < ninho and tirol < boi:
    print("Vai de tirol parça, só R$",barato)
