# class Funcionario:
#     def __init__(self,nome, cargo, salario):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = salario
    
#     def altera_salario(self, novo_salario):
#         salario_ant = self.salario
#         self.salario = novo_salario
#         print(f"O Salário de R${salario_ant}, foi ajustado para {self.salario}")
        
#     def altera_cargo(self, novo_cargo):
#         self.cargo = novo_cargo

# funcionario1 = Funcionario('jose','analista',1000.00)
# funcionario1.altera_salario(3000.00)

# class Animal:
#     def __init__(self,nome):
#         self.nome = nome
    
#     def emitir_som(self):
#         print(f'{self.nome} diz: barulho!')
    
# class Cachorro(Animal):
#     pass
# class Gato(Animal):
#     pass

# dog = Cachorro("Rex")
# cat = Gato("Tom")

# dog.emitir_som()
# cat.emitir_som()

class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descricao(self):
        return f"{self.marca} {self.modelo}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # Chama o construtor da classe pai
        self.portas = portas

    def descricao(self):
        return f"{super().descricao()} - {self.portas} portas"

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def descricao(self):
        return f"{super().descricao()} - Tipo: {self.tipo}"

# Uso das classes
if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 4)
    bicicleta = Bicicleta("Caloi", "C20", "Montanha")

    print(carro.descricao())
    print(bicicleta.descricao())
