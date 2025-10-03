# --- CAPTURA E TRANSFORMAÇÃO DE DADOS (SELIC) ---
import pandas as pd
from datetime import date

# URL da API do Banco Central do Brasil (BCB) para a taxa Selic
API_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

# 1. Captura e Inspeção
df_selic = pd.read_json(API_URL)

print("--- 1. Inspeção Inicial ---")
print(df_selic.info())
# Nota: O campo 'data' (object) precisaria ser convertido para datetime para análise temporal.


# 2. Transformação: Criação de Colunas de Metadados
data_extracao = date.today()
df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autor"

print("\n--- 2. Após Adicionar Metadados ---")
print(df_selic.info())
print("\nPrimeiras linhas com colunas novas:")
print(df_selic[['data', 'valor', 'responsavel']].head())


# 3. Limpeza (Demonstração com DataFrame de Exemplo)
data_vendas = {
    'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E'],
    'quantidade': [3, 1, 4, 3, 2],
    'receita_total': [120, 80, 60, 120, 90]
}
df_vendas = pd.DataFrame(data_vendas)

print("\n--- 3. Limpeza de Duplicatas ---")
print(f"Linhas antes da limpeza: {len(df_vendas)}")

# Drop_duplicates: Remove duplicatas (mantendo a última ocorrência)
df_vendas.drop_duplicates(keep='last', inplace=True)
print(f"Linhas após a limpeza: {len(df_vendas)}")
