import os


def adicionar_item(compras,i):
    item = input("Digite o item:_>")
    valor = input("Digite o valor:_>")
    compras[i] = {"item":item,"valor":valor}
    op2 = input("Deseja continuar? (s/n)_>")
    i+=1
    while op2 !='s' and op2 !='n':
        print("Operação inválida")
        op2 = input("Deseja continuar? (s/n)_>")
    if op2 == 'n':
        os.system('cls')
    else:
        os.system('cls')
        
    return compras,i    