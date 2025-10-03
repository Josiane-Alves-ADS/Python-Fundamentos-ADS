# --- ESTRUTURAS DE CONJUNTOS (SETS) ---

# Criando, adicionando e verificando elementos em um conjunto (set)
meu_conjunto = set()
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
meu_conjunto.add(10) # Tentativa de duplicidade é ignorada

print("Conjunto após adicionar elementos:", meu_conjunto)
elemento = 20
print(f"O elemento {elemento} está no conjunto? {elemento in meu_conjunto}")
meu_conjunto.remove(20)
print("Conjunto após remover o elemento 20:", meu_conjunto)


# --- ESTRUTURAS DE MAPEAMENTO (DICTIONARIES) ---

# Demonstração de diferentes métodos de criação de dicionários
print("\n--- Criação de Dicionários ---")

dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25

dici_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))

print(f"Dicionário criado: {dici_4}")
