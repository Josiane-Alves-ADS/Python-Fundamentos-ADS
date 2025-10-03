# --- ESTRUTURA DE REPETIÇÃO WHILE ---
# Demonstra o loop while para processar inputs até que a condição seja zero.

print("--- Demonstração do loop WHILE (Digite 0 para sair) ---")
numero = -1 # Valor inicial diferente de zero para entrar no loop

while numero != 0:
    try:
        numero = int(input("Digite um número (ou 0 para parar): "))
        if numero == 0:
            break
        
        # Estrutura de checagem:
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
            
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

print("\nFim da execução do loop while.")


# --- CLASSIFICAÇÃO DE FILMES COM FOR E BREAK INTERATIVO ---

print("\n--- Classificador de Filmes ---")
filmes = ["Chuck", "Meu Malvado Favorito", "Super Mario", "Sexta Feira 13", "Scarface"]

for filme in filmes:
    print("-" * 20)
    classificacao_str = input(f"Classifique '{filme}' de 1 a 5? (ou 0 para parar): ")

    if classificacao_str == '0':
        print(f"Classificação interrompida. Finalizando o loop.")
        break  # Encerra o loop principal com "break"

    try:
        classificacao = int(classificacao_str)
        if 1 <= classificacao <= 5:
            print(f"Você classificou '{filme}' com {classificacao} estrelas.")
        else:
            print("Classificação inválida. Insira um número entre 1 e 5.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

print("Fim da classificação.")
