#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# 1L = 3M²
# lata = 18L
#lata = 80rs

metros_quadrados = int(input("Coloque aqui os m² a ser pintado:"))
litros = (metros_quadrados / 3)
quanti_latas = litros / 18
preço_total = quanti_latas * 80

print("Para pintar",metros_quadrados,"m², será necessario",quanti_latas,"latas. Com um custo total de : R$",preço_total,".")