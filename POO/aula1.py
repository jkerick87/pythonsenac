from datetime import datetime

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        # self.ano = ano
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}, tenho {self.idade} anos.")
    
    def ano_nascimento(self):
        ano_atual = (datetime.now().year - self.idade)
        print(f"O ano de nascimento é: {ano_atual}")
        
        
nome = input("Nome: ")
idade = int(input("Idade: "))
pessoa1 = Pessoa(nome,idade)
# print(pessoa1.nome)
# print(pessoa1.idade)
pessoa1.ano_nascimento()
