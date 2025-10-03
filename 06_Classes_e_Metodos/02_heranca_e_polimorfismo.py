# --- HERANÇA E POLIMORFISMO (SOBRESCRITA DE MÉTODOS) ---

# 1. HERANÇA BÁSICA (Demonstração do Polimorfismo)
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_barulho(self):
        # Método genérico que será sobrescrito
        return "Fazendo barulho..."

class Cachorro(Animal):
    # Sobrescreve o método da classe Pai
    def fazer_barulho(self):
        return "Latir"

class Gato(Animal):
    # Sobrescreve o método da classe Pai
    def fazer_barulho(self):
        return "Miar"

# Testando a herança
rex = Cachorro("Rex")
whiskers = Gato("Whiskers")
print(f"\n{rex.nome} (Cachorro) faz: {rex.fazer_barulho()}")
print(f"{whiskers.nome} (Gato) faz: {whiskers.fazer_barulho()}")


# 2. HERANÇA COM MÉTODO SUPER()
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h"

class Carro(Veiculo):
    # __init__ da classe filha chama o __init__ da classe pai (Veiculo)
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia
        
    # Sobrescreve o acelerar para incluir a potência
    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia

# Criando objetos e testando a herança complexa
carro1 = Carro("Toyota", "Corolla", 2022, 100) # Potência 100
carro1.acelerar(10) # 10 + 100 = 110km/h

print("\n--- Herança de Veículos ---")
print("Status do Carro:")
print(carro1.status()) 
# Velocidade deve ser 110, demonstrando a herança e o super().
