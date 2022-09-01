#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia_semana = int(input("Ponha aqui seu numero e te direi a semana correspondete:"))

if dia_semana == 1 :
    print("O dia é Domingo")
elif dia_semana == 2 :
    print("Seu dia é Segunda")
elif dia_semana == 3 :
    print("Seu dia é Terça")
elif dia_semana == 4 :
    print("Seu dia é Quarta")
elif dia_semana == 5 :
    print("Seu dia é Quinta")
elif dia_semana == 6 :
    print("Seu dia é Sexta")
elif dia_semana == 7 :
    print("Seu dia é Sabado")
else:
    print("Numero invalido")
