valor = int(input("Digite o valor atual da sua bolsa auxílio"))
if valor < 1000:
    t1 = valor * 1.15
    print("O valor recebeu um aumento de 15%")
    print("Valor após aumento: R$", t1)
elif valor > 1000:
    t2 = valor * 1.1
    print("O valor recebeu um aumento de 15%")
    print("Valor após aumento: R$", t2)
