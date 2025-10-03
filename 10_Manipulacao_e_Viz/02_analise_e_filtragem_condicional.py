# --- ANÁLISE E FILTRAGEM CONDICIONAL ---
import pandas as pd

# DataFrame de Exemplo (com dados limpos)
data_vendas = {
    'nome': ['Produto B', 'Produto C', 'Produto A', 'Produto E'],
    'quantidade': [1, 4, 3, 2],
    'tipo_item': ['Vestuário', 'Alimento', 'Eletrônico', 'Alimento'],
    'receita_total': [80, 60, 120, 90]
}
df = pd.DataFrame(data_vendas)


# 1. Extração de Informações por Índice (.loc)
print("--- 1. Extração de Linhas (loc) ---")
print("Linha com índice 1:")
print(df.loc[1])


# 2. Criação de Coluna Calculada
# Coluna 'preco_unitario'
df['preco_unitario'] = df['receita_total'] / df['quantidade']
print("\n--- 2. Coluna Calculada ('preco_unitario') ---")
print(df)


# 3. Filtragem Condicional (Seleção Booleana)
# Seleciona itens cujo preço unitário é maior que 50
itens_acima_de_50 = df[df['preco_unitario'] > 50]

print("\n--- 3. Itens com Preço Unitário > R$50 ---")
print(itens_acima_de_50)


# Demonstração de Filtro (Selic) - Usando a lógica booleana
# Este código apenas demonstra o filtro, sem rodar a API novamente.
# teste = df_selic['valor'] < 0.01
# print(f"Tipo de objeto do filtro: {type(teste)}") # pd.Series (Booleana)
