# --- MÓDULO PADRÃO: MATH (DEMONSTRAÇÃO DE IMPORTAÇÃO) ---

# 1. Importação padrão (import [módulo])
import math

print("--- Importação 1: math.funcao() ---")
print(f"Raiz quadrada de 25: {math.sqrt(25)}")
print(f"Logaritmo de 1024 na base 2: {math.log2(1024)}")


# 2. Importação com alias (import [módulo] as [apelido])
import math as m

print("\n--- Importação 2: m.funcao() ---")
print(f"Cosseno de 45 graus: {m.cos(45)}")
print(f"Valor de Pi: {m.pi}")


# 3. Importação seletiva (from [módulo] import [função])
from math import sqrt, log2, cos

print("\n--- Importação 3: funcao() direta ---")
print(f"Raiz quadrada de 25: {sqrt(25)}")
print(f"Logaritmo de 1024 na base 2: {log2(1024)}")
print(f"Cosseno de 45 graus: {cos(45)}")
