import json

def menu():
    print("Menu:")
    print("1. Criar conta")
    print("2. Consultar saldo")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Sair")
    
def carregar_contas():
    try:
        with open('contas.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError: 
        return {}
    except json.JSONDecodeError: 
        return {}
    
def salvar_arquivo(contas):
    with open('contas.txt', 'w') as file:
        json.dump(contas, file)

def criar_conta(contas):
    nome = input("Digite o nome do titular: ")
    numero_conta = input("Digite o número da conta: ")
    saldo = float(input("Digite o saldo inicial: "))

    contas[numero_conta] = {
        "nome": nome,
        "saldo": saldo
    }

    salvar_arquivo(contas)
    print("Conta criada com sucesso!")

def consultar_conta(contas):
    numero_conta = input("Digite o número da conta para consulta: ")
    if numero_conta in contas:
        conta = contas[numero_conta]
        print(f"Nome: {conta['nome'].upper()}, Saldo: {conta['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

def depositar_dinheiro(contas):
    conta_alvo = input("Digite a conta: ")
    
    if conta_alvo in contas :
        novo_valor = float(input("Digite o valor do deposito:"))
        if novo_valor > 0:
            contas[conta_alvo]['saldo'] += novo_valor
            print(f"Depósito de {novo_valor} realizado com sucesso")
            salvar_arquivo(contas)
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")
    else:
        print("Conta não encontrada.")
        

def sacar_dinheiro(contas):
   conta_alvo = input("Digite a conta: ")
   if conta_alvo in contas :
        novo_valor = float(input("Digite o valor do saque:"))
        if contas[conta_alvo]['saldo'] > novo_valor:
            contas[conta_alvo]['saldo'] -= novo_valor
            print(f"Saque de {novo_valor} realizado com sucesso")
            salvar_arquivo(contas)
        else:
            print("Saldo Insuficiente!!!")
   else:
    print("Conta não encontrada.")
       
def main():
    contas = carregar_contas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_conta(contas)

        elif opcao == '2':
            try:
                consultar_conta(contas)
            except UnboundLocalError:
                print("Conta não existe!!!")
                
        elif opcao == '3':
                depositar_dinheiro(contas)
        
        elif opcao == '4':
            sacar_dinheiro(contas) 
            
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")