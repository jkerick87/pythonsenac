import os

opcao = None
while opcao !='sair' :
    print('')
    opcao = input("escolha o numero ou digite sair:")
    if opcao == '1':
        contador = 1
        while contador <= 10:
            print(contador,end=" ")
            contador+=1
    elif opcao =='2':
        senha=1234
        while True:
            valor = int(input("Entre com a senha:"))
            if valor == senha:
                print("Voce acertou!!!")
                break
            else:
                print("Continue Tentando!!!")
    
    elif opcao =='3':
        numero = 0
        while True:
            valor = int(input("Entre com um numero inteiro ou 0 para sair: "))
            if valor != 0:
                numero+=valor
            else:
                print(f"A soma do(s) numero(s) digitado foi {numero}")
                break
            
    elif opcao =='4':
        i = 2
        while i <=20:
            if i%2 == 0:
                print(i,end=' ')
            i+=1    
                
    elif opcao =='5':
        lista = []
        op = None
        while True:
            valor = input("Digite o nome na lista ou digite sair: ")
            if valor!= 'sair':
                lista.append(valor)
            else:
                break
        print(f"Foram Digitado(s) {len(lista)} elemento(s)")
        print(f"Os valor(es) da lista: {lista}")        
    elif opcao == 'sair':
        os.system('cls')