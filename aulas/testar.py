import os
import msvcrt
import funcoes

lista = {}
i=1

while True:
    print("Digite a opção: \n #1 - Adicionar item \n #2 - Remover item\n #3 - Exibir lista\n #4 - Sair")
    op = int(input("_>"))
    if op == 1:
        while True:
            lista,i = funcoes.testar_item(lista,i)
            for item, valor in lista.items():
                #item = lista.get('item')
                print(f"{valor['item']}, {valor['valor']}")
            