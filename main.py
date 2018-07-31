from WordList import WordList

wordlist = WordList()

#Leitura do arquivo
arquivo = open("arquivo.txt", "r")
texto = arquivo.read()

#Remoção de acentos
texto = wordlist.strip_accents(texto)

#Separação por espaços
palavras = texto.split()

array = wordlist.verificaItems(palavras)
array = wordlist.removeMaiusculo(array)

# Criar wordlist
array = wordlist.wordlist(array,8)

#wordlist.printarArray(array)

wordlist.preencherArquivo(array)

