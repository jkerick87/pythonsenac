# lista = []
# while True:
#     valor = input("Digite um número ou sair para finalizar:").lower()
#     if valor == 'sair':
#         break
#     else:
#         lista.append(valor)
# #print(lista)
# while True:
#     try:
#         indice = int(input("Digite o indice ou sair para finalizar:").lower())
#         if indice == 'sair':
#             break
#         else:
#             print(f"O valor que está no índice:{indice} é:{lista[indice]}")
#     except IndexError:
#         print("Não existe elemento nesse índice")
#     except ValueError:
#         print("Digite apenas números")
        
################################################################################################
# class SenhaFracaError(Exception):
#     """Exceção levantada quando a senha não atende aos critérios de segurança."""
#     pass

# def verificar_senha(senha):
#     if len(senha) < 8:
#         raise SenhaFracaError("A senha deve ter pelo menos 8 caracteres.")
#     if not any(c.islower() for c in senha):
#         raise SenhaFracaError("A senha deve conter pelo menos uma letra minúscula.")
#     if not any(c.isupper() for c in senha):
#         raise SenhaFracaError("A senha deve conter pelo menos uma letra maiúscula.")
#     if not any(c.isdigit() for c in senha):
#         raise SenhaFracaError("A senha deve conter pelo menos um número.")
    
#     print("Senha forte!")

# # Exemplo de uso
# try:
#     senha_input = input("Digite a senha: ")
#     verificar_senha(senha_input)
# except SenhaFracaError as e:
#     print(f"Erro: {e}")

################################################################################################

def calculo(num1,num2,op):
    if op =='+':
        resultado = num1+num2
    elif op =='-':
        resultado = num1-num2
    elif op =='*':
        resultado = num1*num2
    elif op =='/':
        resultado = num1-num2

