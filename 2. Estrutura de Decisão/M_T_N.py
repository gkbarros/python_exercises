#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


print("Digite qual turno vc estuda")
print("M para Manha, T para Tarde, N para noite")

turno = input("Digite M ou T ou N aqui :")

if turno == "M":
    print("Bom dia")
elif turno == "T":
    print("Boa tarde")
elif turno =="N":
    print("Boa noite carai")
else:
    print('Valor invalido')


