# --- FUNÇÕES BUILT-IN E DEFINIÇÃO BÁSICA ---

# Demonstração de função built-in (len)
numeros = [1, 2, 3, 4, 5]
comprimento = len(numeros)
print(f"O comprimento da lista é: {comprimento}")

# --- FUNÇÃO DEFINIDA PELO USUÁRIO (com retorno e parâmetro) ---

# Definindo uma função para somar dois números
def soma(a, b):
    """Retorna a soma de dois números."""
    resultado = a + b
    return resultado

# Chamando a função
resultado_soma = soma(5, 3)
print(f"\nA soma de 5 e 3 é: {resultado_soma}")
# Resultado esperado: A soma de 5 e 3 é: 8


# --- FUNÇÃO PARA CHECAGEM DE PARIDADE ---

def e_par(numero):
    """Retorna True se o número for par, False caso contrário."""
    if numero % 2 == 0:
        return True
    else:
        return False

# Teste 1
numero_1 = 123120
if e_par(numero_1):
    print(f"\n{numero_1} é um número par.")
else:
    print(f"\n{numero_1} não é um número par.")

# Teste 2
numero_2 = 1355989
if e_par(numero_2):
    print(f"{numero_2} é um número par.")
else:
    print(f"{numero_2} não é um número par.")
