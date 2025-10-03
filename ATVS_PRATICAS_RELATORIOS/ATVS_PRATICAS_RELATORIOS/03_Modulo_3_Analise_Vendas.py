# CÉLULA 1: Conexão e Criação do Banco de Dados SQLite (Passo 1)
import sqlite3
import pandas as pd # Importa Pandas aqui para uso posterior

# 1.1: Conectar ao banco de dados (o arquivo 'dados_vendas.db' será criado)
conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

# 1.2: Criar a tabela 'vendas1' (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')
print("Tabela 'vendas1' verificada/criada.")

# 1.3: Inserir dados de exemplo na tabela
# NOTA: O 'REPLACE' garante que se a célula for rodada várias vezes, os dados são resetados (opcional)
dados_a_inserir = [
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
]

# Limpar dados antigos e inserir novos (para garantir que o DataFrame não duplique)
cursor.execute("DELETE FROM vendas1")
cursor.executemany('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) 
VALUES (?, ?, ?, ?)
''', dados_a_inserir)

# 1.4: Confirmar as mudanças no BD
conexao.commit()
print("Dados de vendas inseridos no banco de dados.")

# Passo 2 Início: Carregar os dados do SQLite para um DataFrame Pandas
query = "SELECT * FROM vendas1"
df_vendas = pd.read_sql_query(query, conexao)

# Fechar conexão (boa prática)
conexao.close()
print("Dados carregados para o DataFrame Pandas e conexão SQLite fechada.")

# CÉLULA 2: Exploração e Preparação de Dados (Pandas)

print("--- VISUALIZAÇÃO E PRÉ-PROCESSAMENTO ---")

# 2.1: Estrutura e Tipos de Dados
print("\nInformações Iniciais do DataFrame:")
df_vendas.info()

# 2.2: Conversão de Tipos (Limpeza/Tratamento)
# Converte a coluna 'data_venda' para o tipo datetime do Pandas
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
# Extrai o mês da data para facilitar a análise temporal
df_vendas['mes'] = df_vendas['data_venda'].dt.month

print("\nPrimeiras linhas após o tratamento:")
print(df_vendas.head())

# CÉLULA 3: Análise de Dados e Visualização (Pandas, Matplotlib, Seaborn)
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração do estilo dos gráficos (opcional, mas profissional)
sns.set_style("whitegrid")

# --- ANÁLISE 1: Vendas Totais por Categoria (Insights de Desempenho) ---
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().sort_values(ascending=False)
print("\n--- ANÁLISE 1: Vendas Totais por Categoria ---")
print(vendas_por_categoria)

# Visualização 1: Gráfico de Barras (Seaborn/Matplotlib)
plt.figure(figsize=(10, 6))
# Seaborn para criar o gráfico
sns.barplot(x=vendas_por_categoria.index, y=vendas_por_categoria.values, palette="viridis")
plt.title('Vendas Totais por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor Total de Vendas (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# --- ANÁLISE 2: Média de Vendas ao Longo do Tempo (Insights Temporais) ---
vendas_por_mes = df_vendas.groupby('mes')['valor_venda'].mean()
print("\n--- ANÁLISE 2: Média de Vendas Mensais ---")
print(vendas_por_mes)

# Visualização 2: Gráfico de Linha (Matplotlib)
plt.figure(figsize=(10, 6))
# Pandas/Matplotlib para plotar a série temporal
vendas_por_mes.plot(kind='line', marker='o', color='red')
plt.title('Média de Vendas por Mês (Análise Temporal)')
plt.xlabel('Mês')
plt.ylabel('Média de Vendas (R$)')
plt.grid(True)
plt.show()

# --- ANÁLISE 3: Estatísticas Descritivas (Resumo da Distribuição) ---
print("\n--- ANÁLISE 3: Estatísticas Descritivas de Valor de Venda ---")
print(df_vendas['valor_venda'].describe())
