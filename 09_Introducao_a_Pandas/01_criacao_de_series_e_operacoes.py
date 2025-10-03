# --- INTRODUÇÃO ÀS SERIES (ESTRUTURA FUNDAMENTAL DO PANDAS) ---
import pandas as pd

# 1. Criação de Series a partir de uma Lista (Indexação Padrão)
data_list = [10, 20, 30, 40, 50]
series_list = pd.Series(data_list)
print("--- Series criada de uma Lista ---")
print(series_list)


# 2. Criação de Series a partir de um Dicionário (Indexação Nomeada)
data_dict = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}
series_dict = pd.Series(data_dict)
print("\n--- Series criada de um Dicionário ---")
print(series_dict)


# 3. Aplicação prática: Séries e Operações Estatísticas
dados_alunos = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]
}
# Cria uma Series usando nomes como índice e idades como valores
serie_idades = pd.Series(dados_alunos['Idade'], index=dados_alunos['Nome'])

print("\n--- Série de Idades com Nomes como Índice ---")
print(serie_idades)

# Cálculo de estatística básica
media_idades = serie_idades.mean()
print("\nMédia de Idades (usando .mean()):", media_idades)
