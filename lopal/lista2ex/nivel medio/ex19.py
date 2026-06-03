porta = ["80", "443"]
tries = ""
while tries != porta:
    tries = input("Digite a portas de rede: ")
    if tries == "80" or tries == "443":
        print("Porta liberada")
        break
    else:
        print("Acesso negado")
