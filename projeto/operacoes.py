import json

def menu():
    print("Menu:")
    print("1. Criar conta")
    print("2. Consultar saldo")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Sair")

def criar_conta(contas):
    nome = input("Digite o nome do titular: ")
    numero_conta = input("Digite o número da conta: ")
    saldo = float(input("Digite o saldo inicial: "))

    contas[numero_conta] = {
        "nome": nome,
        "saldo": saldo
    }

    # Salvar no arquivo
    with open('contas.txt', 'w') as file:
        json.dump(contas, file)

    print("Conta criada com sucesso!")

def consultar_conta(contas):
    numero_conta = input("Digite o número da conta para consulta: ")
    if numero_conta in contas:
        conta = contas[numero_conta]
        print(f"Nome: {conta['nome']}, Saldo: {conta['saldo']:.2f}")
    else:
        print("Conta não encontrada.")
        
    return conta['nome'],conta['saldo']

def carregar_contas():
    try:
        with open('contas.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def depositar_dinheiro(contas):
    cliente = consultar_conta(contas)
    
    print(cliente)
    print("Valor Atualizado!!!")
    

def main():
    contas = carregar_contas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            try: 
                criar_conta(contas)
            except UnboundLocalError:
                print("Conta não existe.") 
                 
        elif opcao == '2':
            try:
                nome,saldo = consultar_conta(contas)
                print(f'Saldo: {saldo}')
            except UnboundLocalError:
                print("Conta não existe.")
                
        elif opcao == '3':
            depositar_dinheiro(contas)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")