#soma = 0
#for i in range(1,11):
#    soma += i 
#    a = 0
#    b = 10
#    print(soma)
#    print(a) 
#
#print(soma)
#print(a)

#palavra = 'camarada'
#
#for i in range(len(palavra)):
#    print(f"A LETRA:{palavra[i]} e o indice é {i}")
#    
#for letra, z in enumerate(palavra):
#    print(f"A LETRA:{z} e o indice é {letra}")
    
while True:
    frase = input("Entre com a frase: ").lower()
    vogais = "aeiou"
    contador = 0
    contador2 = 0

    for letra in frase:
        if letra in vogais:
            contador +=1
        else:
            contador2 +=1

    print(f"Há {contador} vogais na frase e {contador2} consoantes")