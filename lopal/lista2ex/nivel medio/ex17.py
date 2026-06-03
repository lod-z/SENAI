bob = 0
alice = 0
voto = 1
while voto != 0:
    voto = input("Vote em um dos candidatos para ser o líder do squad.\n1 - Alice\n2 - Bob\n")
    if voto == "1" or voto == "Alice":
        alice += 1
        print("Voto confirmado!")
    elif voto == "2"or voto == "Bob":
        bob += 1
        print("Voto confirmado")
    else:
        print("A quantidade de votos foram:\nBob - ", bob, "votos\nAlice - ", alice, "votos.")
        print("Saindo......")
        break
