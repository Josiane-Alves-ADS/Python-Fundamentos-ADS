# --- LEITURA DE DADOS ESTRUTURADOS COM PANDAS ---
import pandas as pd

# URL de exemplo (Lista de bancos falidos do FDIC)
# Nota: Este código é para demonstrar a função; a URL e o conteúdo podem mudar.
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

# A função read_html retorna uma lista de DataFrames, um para cada tabela na URL.
try:
    print("Tentando ler tabela da URL...")
    dfs = pd.read_html(url)
    
    print(f"Tipo de objeto retornado: {type(dfs)}")
    print(f"Número de tabelas encontradas: {len(dfs)}")

    # O DataFrame é geralmente o primeiro item da lista
    df_bancos = dfs[0]
    
    print("\n--- Análise do DataFrame (df_bancos) ---")
    print(f"Dimensões do DataFrame (Linhas, Colunas): {df_bancos.shape}")
    print("\nPrimeiras 5 linhas (df_bancos.head()):")
    print(df_bancos.head())

except Exception as e:
    print(f"Erro ao tentar ler a URL (o site pode estar offline ou o formato mudou): {e}")

# Demonstração dos tipos de dados (dtypes)
if 'df_bancos' in locals():
    print("\nTipos de dados (df_bancos.dtypes):")
    # Imprime apenas as primeiras 4 colunas para concisão no portfólio
    print(df_bancos.dtypes.head(4))
