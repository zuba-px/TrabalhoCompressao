arquivo = open("./THERING.txt", "r")
texto = arquivo.read()

texto_comprimido = open("./texto_comprimido.txt", "w")
texto_descomprimido = open("./texto_descomprimido.txt", "w")

espacos = 0
frase_comprimida = ""

#Criando a lista com as frases do arquivo
#Comprimindo
lista1 = []
for linha in texto:
    for caracter in linha:
        lista1.append(caracter)
        
for caracter in lista1:
    if caracter == " ":
        espacos +=1
    elif espacos > 0:
        frase_comprimida += "x"
        frase_comprimida += str(espacos)
        espacos = 0
    
    if caracter != " ":
        frase_comprimida += caracter
        
texto_comprimido.write(frase_comprimida)


#Descomprimindo
lista2 = []
i = 0

while i < len(frase_comprimida):
    caracter_atual = frase_comprimida[i]
    if caracter_atual == "x":
        espacos_str = ""
        j = i + 1
        
        while j < len(frase_comprimida) and frase_comprimida[j].isdigit():
            espacos_str += frase_comprimida[j]
            j +=1
            espacos = int(espacos_str)
            lista2.extend([" "] * espacos) #Tirando essa linha o arquivo não sofre perda de dados porém é removido todos os espaços
        i = j - 1 # Deixar - 1 o arquivo fica maior
        #i = j + 1 #Deixar + 1 o arquivo ficar menor doq o original porém com perda de dados
    else:
        lista2.append(caracter_atual)
    i +=1
    
#def funcao(g):
 #   j = i + 1
  #  caracter_atual * 1
   # return caracter_atual[g]
    
frase_descomprimida = "".join(lista2)

texto_descomprimido.write(frase_descomprimida)
print(lista1)
print(lista2)

#Fechando os arquivos
arquivo.close()
texto_comprimido.close()
texto_descomprimido.close()  
