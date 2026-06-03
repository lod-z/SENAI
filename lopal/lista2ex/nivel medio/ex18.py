orierdepedavul = input("Digite uma palavra: ")
luvadepedreiro = orierdepedavul[::-1]
if orierdepedavul in luvadepedreiro:
    print(luvadepedreiro, "é um palindromo")
else:
    print("Não é um palindromo")
