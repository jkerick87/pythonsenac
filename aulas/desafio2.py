minhaLista = [76,92.3,"oi",True,4,76]
print(minhaLista)

minhaLista.append("pera")
minhaLista.append(76)
print(minhaLista)
minhaLista.insert(0,99)
print(minhaLista)
indice = minhaLista.index("oi")
print("O indice:",indice)
minhaLista.remove(True)
print(minhaLista)

uma_lista = [4,2,8,6,5]
uma_lista = uma_lista  + ['gato','bode','bola',4]
print(uma_lista)
print(uma_lista.count(4))

nome = "AAAAAAA"
print(nome.count("A"))
