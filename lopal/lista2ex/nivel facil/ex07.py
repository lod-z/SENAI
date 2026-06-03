print("Digite um número de 1 a 223 para o par de octeto")
octt = int(input())
if octt <= 126:
    print("Classe A")
elif octt <= 191:
    print("Classe B")
elif octt <= 223:
    print("Classe C")
