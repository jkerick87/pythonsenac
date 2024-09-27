frutas = ["maca","banana","laranja"]
frutas.append("uva")
frutas.remove("banana")
print(frutas)
print("Esse é o segundo elemento:", frutas[1])
frutas.reverse()
print(frutas)

cores = ("vermelho","verde","azul")
print(f"O primeiro elemento da lista é: {cores[0]} e o ultimo é: {cores[-1]}")
cores2 = ("amarelo","roxo")
cores3 = cores + cores2
print(cores3)
cor1,cor2,cor3 = cores
print(cor1)