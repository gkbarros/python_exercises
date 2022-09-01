#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
 # Média de Aproveitamento  Conceito
 # Entre 9.0 e 10.0        A
 # Entre 7.5 e 9.0         B
 # Entre 6.0 e 7.5         C
 # Entre 4.0 e 6.0         D
 # Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito #correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou #“REPROVADO” se o conceito for D ou E.

nota1 = int(input("Ponha aqui sua 1 nota"))
nota2 = int(input("Ponha aqui sua 2 nota"))
nota_final = (nota1 + nota2) / 2
status = "Aprovado"
conceito = "A"

if nota_final >7.5 and nota_final < 9:
    conceito = "B"
elif nota_final >= 6 and nota_final <= 7.5:
    conceito = "C"
elif nota_final >= 4 and nota_final <= 6:
    conceito = "D"
    status = "Reprovado"
elif nota_final >= 4 and nota_final <= 0:
    conceito = "E"
    status = "Reprovado"

print("Sua primeira nota foi",nota1,"Sua segunda nota foi",nota2," Sua media foi",nota_final,"Seu conceito é:",conceito,"E voce esta",status,)