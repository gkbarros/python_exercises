#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
print("Olá, me de as duas notas e direi se foi aprovado ou não")
nota1 = int(input("Coloque a primeira nota parcial aqui: "))
nota2 = int(input("Agora a segunda nota aqui: "))
media = (nota1 + nota2) / 2

if media == 10:
    print ("Parabens , sua media foi",media)
else:
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
