mercado = []
def menu():
    while True:
        print("===LISTA DO SUPERMERCADO===\n1.Listar Produtos \n2.Sair.")
        escolha = input("Escolha uma das opções. \n")
        if escolha == "1" or escolha == "Listar Produtos" or escolha == "Listar":
            mercado.append(input("Liste seus produtos abaixo\n"))
        elif escolha =="2" or escolha == "Sair" or escolha == "sair":
            for escolha in mercado:
                print(escolha)
            break
        else:
            print("\nOpção não encontrada...\n")
menu()
