import os
import msvcrt
import funcoes

compras = {}
op = None
i=1
while op != 4:
    print("Digite a opção: \n #1 - Adicionar item \n #2 - Remover item\n #3 - Exibir lista\n #4 - Sair")
    op = int(input("_>"))
    if op == 1:
        while True:
            compras,i = funcoes.adicionar_item(compras,i)
            break
    elif op == 2:
        while True:
            selecao = input("Digite o nome do item que deseja remover: _>")
            for chave in list(compras.keys()):  
                if compras[chave]["item"] == selecao:
                    del compras[chave]
                else: 
                    print("Valor nao existe")
                    print("Depois da remoção:", compras)

    elif op == 3:
        os.system('cls')
        for item, valor in compras.items():
            print(f"{valor['item']}: {valor['valor']}")
        print("Pressione qualquer tecla para continuar...")
        msvcrt.getch()   
        os.system('cls')
    elif op == 4:
        break
    else:
        os.system('cls')
        print("Selecione uma das opções!!!\nPressione qualquer tecla para continuar...")
        msvcrt.getch()   
        os.system('cls')
#     else:
#         break
# print(f"Foram Digitado(s) {len(lista)} elemento(s)")
# print(f"Os valor(es) da lista: {lista}")        