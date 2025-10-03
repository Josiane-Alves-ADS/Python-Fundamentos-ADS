# --- VISUALIZAÇÃO DE DADOS EM PYTHON (MATPLOTLIB, PANDAS, SEABORN) ---
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
import numpy as np # Adicionando numpy para gerar dados limpos

# --- 1. MATPLOTLIB (Núcleo) ---
print("--- 1. Matplotlib Básico ---")
# Gerando dados aleatórios para um gráfico de linha simples
np.random.seed(42)
dados1 = np.random.randint(1, 100, size=20)
dados2 = np.random.randint(1, 100, size=20)

plt.figure(figsize=(5, 3))
plt.plot(dados1, dados2, label='Dados Aleatórios')
plt.title('Gráfico de Linha (Matplotlib Puro)')
plt.legend()
# plt.show() # Comentado para rodar no GitHub


# --- 2. PANDAS PLOT (Integração Rápida com DataFrame) ---
print("\n--- 2. Pandas Plot ---")
dados = {
    'Produto':['A', 'B', 'C'],
    'qtde_vendida':[33, 50, 45]
}
df = pd.DataFrame(dados)

# Gráfico de Barras
df.plot(x='Produto', y='qtde_vendida', kind='bar', title='Vendas por Produto (Barra)')
# df.plot(x='Produto', y='qtde_vendida', kind='pie', y='qtde_vendida', title='Vendas por Produto (Pizza)') # O Pandas Pie plot requer tratamento do eixo y
# df.plot(x='Produto', y='qtde_vendida', kind='line', title='Vendas por Produto (Linha)')
# plt.show() # Comentado


# --- 3. SEABORN (Visualização Estatística Estilizada) ---
print("\n--- 3. Seaborn (Barplot) ---")
sns.set(style="whitegrid") 
df_tips = sns.load_dataset('tips')

# Exemplo de Subplots e Agregação (Polimorfismo do estimator)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# 1. Média (Padrão)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0], ci=None).set_title('Média')
# 2. Soma
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum, ci=None).set_title('Soma')
# 3. Contagem
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len, ci=None).set_title('Contagem')

# Exemplo de plotagem final com estilo e customização
plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df_tips, estimator=sum, ci=None, palette="Set2")
plt.xlabel('Período (Time)')
plt.ylabel('Total de Gastos (Soma)')
plt.title('Total de Gastos por Período (Almoço ou Jantar)')

# plt.show() 
print("\nTrês bibliotecas de visualização demonstradas com sucesso.")
