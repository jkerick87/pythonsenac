# class Animal:
#     def fazer_som(self):
#         pass
# class Cachorro(Animal):
#     def fazer_som(self):
#         print("Au Au!")

# class Gato(Animal):
#     def fazer_som(self):
#         print("Miau!")
    
# animais = [Cachorro(),Gato()]

# for animal in animais:
#     animal.fazer_som()
#############################################################################################
# class Veiculo:
#     def ligar_veiculo(self):
#         pass
# class Carro(Veiculo):
#     def ligar_veiculo(self):
#         print("Carro ligado")
# class Moto(Veiculo):
#     def ligar_veiculo(self):
#         print("Moto ligada")
# veiculos = [Carro(), Moto()]
# for veiculo in veiculos:
#     veiculo.ligar_veiculo()
# class Pessoa:
#     def __init__(self, nome):
#          self.nome = nome
#     @property
#     def nome(self):
#         return self._nome
#     @nome.setter
#     def nome(self, novo_nome):
#         if isinstance(novo_nome, str) and novo_nome.strip():
#             self._nome = novo_nome
#         else:
#             print("Nome inválido")

# pessoa = Pessoa("Alice")
# print(pessoa.nome)
# pessoa.nome = "Maria"
# print(pessoa.nome)
# pessoa.nome = ""

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
         return self.__nome
     
    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}, Idade: {self.__idade}")
pessoa = Pessoa("Alice", 30)

print(pessoa.nome)