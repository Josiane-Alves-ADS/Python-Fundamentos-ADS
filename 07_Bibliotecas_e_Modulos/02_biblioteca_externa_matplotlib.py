# --- USO DE BIBLIOTECA EXTERNA: MATPLOTLIB PARA VISUALIZAÇÃO ---

# É importante notar que, para rodar este código, a biblioteca precisa ser instalada
import matplotlib.pyplot as plt

# --- Gráfico 1: Linhas ---
# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Configuração
plt.figure(figsize=(6, 4)) # Define o tamanho da figura (opcional)
plt.plot(x, y, label='Variação de Valores')

# Títulos e Rótulos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Exemplo de Gráfico de Linha')
plt.legend()
plt.grid(True)
# O plt.show() será comentado no código do GitHub, mas é essencial para rodar localmente.
# plt.show() 
print("Primeiro gráfico configurado (Linha).")


# --- Gráfico 2: Barras ---
# Dados de exemplo
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [120, 90, 150, 80, 200]

# Configuração
plt.figure(figsize=(7, 5))
plt.bar(meses, vendas, color='royalblue', label='Vendas Mensais')

# Títulos e Rótulos
plt.xlabel('Mês')
plt.ylabel('Vendas (em unidades)')
plt.title('Vendas Mensais (Gráfico de Barras)')
plt.legend()
# plt.show() 
print("Segundo gráfico configurado (Barras).")
print("\nPara visualizar os gráficos, o repositório deve ser clonado e o código executado localmente.")
