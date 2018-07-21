import unicodedata

class WordList:

    # Verificando se o item é um digito ou uma palavra e adicionando no array
    def verificaItems(self,palavras):
        array = []
        for x in range(len(palavras)):
            palavra = "".join(e for e in palavras[x] if e.isalpha() or e.isdigit())
            array.append(palavra)
        return array

    # Função para remover acentos
    def strip_accents(self,s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')

    # Substituindo os caracteres maiúsculos por minusculos
    def removeMaiusculo(self,array):
        for i in range(len(array)):
            array[i] = array[i].lower()
        return array

    # Criando wordlist com a quantidade de caracteres passada
    def wordlist(self,array,quant):
        palavras = []

        for k in range (len(array)):
            for i in range (len(array)):
                palavra = array[k] + array[i]
                if len(palavra) >= quant:
                    palavras.append(palavra[0:quant-1])

        return palavras

    #Print do array
    def printarArray(self,array):
        for k in range (len(array)):
            print(array[k])

        print("Quantidade de palavras: "+ str(len(array)))