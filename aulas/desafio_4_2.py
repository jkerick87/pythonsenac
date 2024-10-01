import random
import os

aleatorio = random.randint(1,20)
contador = 0
opcao = 's'

while opcao=='s':
    
    while True:
        contador+=1
        valor = int(input("Adivinhe o numero entre 1 e 20:-> "))
        if aleatorio == valor:
            break
        elif aleatorio > valor:
            print("O numero é maior!!! Continue tentando")
        else:
            print("O numero é menor!!! Continue tentando")
            
    print(f"Parabens você acertou, com {contador} tentativa(s)!!! O numero é: {aleatorio}")
    
    opcao = input("Deseja continuar advinhando(s/n)? ->").lower()
    
    while opcao != 's' and opcao !='n':
        #if opcao !='n' or opcao!= 's':
        print("Operação inválida")
        opcao = input("Deseja continuar advinhando(s/n)? -> ").lower()
    if opcao == 's':
        os.system('cls')
        contador = 0
    else:
        os.system('cls')
        print("Até Logo!!!")