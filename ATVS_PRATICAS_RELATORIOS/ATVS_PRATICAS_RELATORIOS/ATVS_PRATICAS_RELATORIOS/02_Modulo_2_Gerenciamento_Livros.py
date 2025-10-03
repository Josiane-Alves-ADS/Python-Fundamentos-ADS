# CÉLULA 1: Classe Livro e Importação de Bibliotecas

# 1. Instalação da Matplotlib (Necessário no Colab se não estiver pré-instalada)
# Embora o Matplotlib geralmente venha pré-instalado no Colab, manter o comando é uma boa prática.
# !pip install matplotlib

# Importação das bibliotecas
import matplotlib.pyplot as plt
from collections import defaultdict # Biblioteca nativa para facilitar a contagem de gêneros

# PASSO 1: Definir a classe Livro
class Livro:
    """
    Classe que representa um livro na biblioteca.
    Define os atributos: título, autor, gênero e quantidade.
    """
    def __init__(self, titulo, autor, genero, quantidade):
        # Construtor (__init__) para inicializar os atributos do objeto.
        self.titulo = titulo.title()    # title() garante capitalização consistente
        self.autor = autor.title()
        self.genero = genero.title()
        self.quantidade = quantidade
    
    def __str__(self):
        # Método especial para representação de string (útil para listar).
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero} | Qtd: {self.quantidade}"

# PASSO 2: Criar a lista de livros
lista_livros = []

print("Estrutura da Classe Livro e lista inicializadas.")

# CÉLULA 2: Funções de Gerenciamento da Biblioteca

def cadastrar_livro(lista_livros, titulo, autor, genero, quantidade):
    """
    Função para cadastrar um novo objeto Livro na lista.
    """
    # Cria uma nova instância da classe Livro (POO)
    novo_livro = Livro(titulo, autor, genero, quantidade)
    lista_livros.append(novo_livro)
    print(f"\nLivro '{titulo.title()}' cadastrado com sucesso!")


def listar_livros(lista_livros):
    """
    Função para listar todos os livros cadastrados.
    Utiliza um loop de repetição (for) para iterar sobre a lista.
    """
    print("\n--- LIVROS CADASTRADOS ---")
    if not lista_livros:
        print("Nenhum livro disponível na biblioteca.")
        return
        
    for livro in lista_livros:
        # Chama o método __str__ definido na classe Livro
        print(livro)


def buscar_livro_por_titulo(lista_livros, titulo_busca):
    """
    Função para buscar um livro pelo título usando uma estrutura de repetição.
    """
    titulo_busca = titulo_busca.title()
    encontrados = []
    
    for livro in lista_livros:
        # Estrutura condicional para verificar se o título coincide
        if titulo_busca in livro.titulo:
            encontrados.append(livro)
            
    print(f"\n--- RESULTADO DA BUSCA por '{titulo_busca}' ---")
    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado com esse título.")

  # CÉLULA 3: Função de Geração de Gráfico (Matplotlib)

def gerar_grafico_genero(lista_livros):
    """
    Gera um gráfico de barras da quantidade de livros por gênero,
    utilizando a biblioteca Matplotlib.
    """
    if not lista_livros:
        print("Não há livros para gerar o gráfico.")
        return
        
    # Lógica de contagem: Usa um dicionário para armazenar a contagem por gênero
    contagem_generos = defaultdict(int) # defaultdict simplifica a contagem
    
    for livro in lista_livros:
        # Adiciona a quantidade do livro ao gênero correspondente
        contagem_generos[livro.genero] += livro.quantidade
        
    # Prepara os dados para o Matplotlib
    generos = list(contagem_generos.keys())
    quantidades = list(contagem_generos.values())
    
    # Criação do Gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(generos, quantidades, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
    
    # Adicionando rótulos e título
    plt.xlabel('Gênero do Livro')
    plt.ylabel('Quantidade Total em Estoque')
    plt.title('Distribuição de Livros por Gênero na Biblioteca')
    
    # Exibe a quantidade exata sobre cada barra
    for i, quantidade in enumerate(quantidades):
        plt.text(i, quantidade + 0.5, str(quantidade), ha='center', va='bottom')
        
    plt.show() # Exibe o gráfico no Colab
    print("\nGráfico de distribuição de livros por gênero gerado.")

# CÉLULA 4: Fluxo de Teste e Execução

print("--- INICIANDO TESTES DO SISTEMA ---")

# 1. Cadastrar Livros (Testa a função de cadastro e a Classe Livro)
cadastrar_livro(lista_livros, "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 5)
cadastrar_livro(lista_livros, "1984", "George Orwell", "Distopia", 3)
cadastrar_livro(lista_livros, "Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 8)
cadastrar_livro(lista_livros, "A Revolução dos Bichos", "George Orwell", "Distopia", 4)
cadastrar_livro(lista_livros, "Cálculo 1", "James Stewart", "Acadêmico", 1)

# 2. Listar Todos os Livros
listar_livros(lista_livros)

# 3. Buscar um Livro (Testa a função de busca e a estrutura condicional)
buscar_livro_por_titulo(lista_livros, "Harry")
buscar_livro_por_titulo(lista_livros, "orwell") # Teste com busca parcial e case-insensitive

# 4. Gerar Gráfico (Testa a função de visualização com Matplotlib)
gerar_grafico_genero(lista_livros)

print("\n--- TESTES CONCLUÍDOS ---")
