# --- INTRODUÇÃO À ORIENTAÇÃO A OBJETOS: CLASSES E CONSTRUTORES ---

# Define uma classe chamada Pessoa.
class Pessoa:
    # O método __init__ é o construtor, chamado ao criar um objeto.
    def __init__(self, nome, idade, genero):
        # Inicializa os atributos da instância
        self.nome = nome
        self.idade = idade
        self.genero = genero
        
    # Método para retornar uma saudação
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."
        
    # Método para alterar um atributo da instância
    def aniversario(self):
        self.idade += 1

# Criação da primeira instância (Objeto)
pessoa1 = Pessoa("João", 30, "Masculino")

# Chamando os métodos
print(pessoa1.cumprimentar()) 
print(f"Idade inicial: {pessoa1.idade}")

# Chamando o método que altera o estado do objeto
pessoa1.aniversario()
print(f"Nova idade após aniversário: {pessoa1.idade}")
