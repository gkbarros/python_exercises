#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.


def am_to_pm(h,m):
    h2 = h / 12
    ap=0
    x=""
    if h2 <= 1:
        ap += 1
    else:
        ap = 0
    if ap == 0:
        x = "PM"
    else:
        x = "AM"
    if h2 <= 1:
        print('Your hours is',h,":",m,x)
    elif h2 > 1 and h2 < 2:
        print('Your hours is',(h-12),":",m,x)

while True:
    print("Type '0' to exit")
    h = int(input('Type your hours here:')) 
    if h == 0:
        break
    m = int(input("Type your minuts here:"))
    print(am_to_pm(h, m))