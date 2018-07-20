arquivo = open("arquivo.txt", "r")

texto = arquivo.read()

palavras = texto.split()
array = []

for x in range(len(palavras)):
    palavra = "".join(e for e in palavras[x] if e.isalpha())
    if palavra != "":
        array.append(palavra)

for k in range(len(array)):
    if len(array[k])==9 or len(array[k]) == 10:
            print(array[k])
