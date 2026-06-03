frase = input("Digite uma frase: ")
contador = 0
for i in frase:
    if i .lower() in "aeiou":
        contador += 1
print(contador)
