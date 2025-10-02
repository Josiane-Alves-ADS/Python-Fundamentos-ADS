# --- MÁQUINA DE VENDA DE INGRESSOS DE CINEMA ---

# 1. Solicita a idade do cliente
# O input é necessário para demonstrar a interatividade e o casting de tipos.
idade = int(input("Por favor, digite sua idade: "))

# 2. Sugestão de filmes baseada na faixa etária
if idade < 12:
    print("Recomendamos o filme infantil 'Toy Story'.")
elif 12 <= idade < 18: # Condição combinada para a faixa adolescente
    print("Recomendamos o filme adolescente 'Harry Potter e a Pedra Filosofal'.")
else:
    print("Recomendamos o emocionante 'O Poderoso Chefão'.")
    
# 3. Verifica a disponibilidade de ingressos (uma condição separada)
quantidade_ingressos = 10 

if quantidade_ingressos > 0:
    print("Ingressos estão disponíveis. Divirta-se no cinema!")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")
