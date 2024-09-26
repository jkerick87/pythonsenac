lista1 = []
# lista1 = [1,"2",3]
# print(type(lista1),lista1)
i=-1
lista2 = [123,"321","SENAC"]

lista3 = ["C",4.65,True,"True","Vamos Aprender",["outra","lista","interna"],lista2]
print(lista3[2:6:2])
print(lista3[3:])
print(lista3[::i])
print(len(lista3))
print(lista3 [: :])

print("LISTA 1:", lista1)
lista1.append("Python")
lista1.append("Java")
lista1.append("PHP")
lista1.append("C#")
print(lista1)

lista1.insert(2,"C++")
print(lista1)

lista1.remove("Java")
print(lista1)

#indice = lista1("PHP")
#print(indice)
#print(L)

a = [1,2,3]
b = a[:]
b[0] = 5
print(a[3])