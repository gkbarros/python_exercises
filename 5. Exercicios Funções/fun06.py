#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
#O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
# Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def pay(vl,dl):
    if dl < 1:
        print(vl)
        return vl
    else:
        vl = vl + (vl * 3/100)+((vl * 0.1/100)*dl)
        print(vl)
        return(vl)

vl = 0
dl = 0
pay_list = []
pay_check = 0
pay_total = 0

while True:
    print('Type 0 to exit')
    vl = int(input('Type here the value :'))
    if vl == 0:
        break
    dl = int(input('Type here days late :'))
    pay_list.append(pay(vl,dl))
    pay_check += 1
    pay_total += pay(vl,dl)

print('A total of '+str(len(pay_list))+' paid debts. With a total value of '+str(pay_total))

print(pay_list)