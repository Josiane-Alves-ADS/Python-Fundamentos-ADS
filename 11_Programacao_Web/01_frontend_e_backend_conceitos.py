# --- PROGRAMAÇÃO WEB: CONCEITOS BÁSICOS (FRONT-END E BACK-END) ---

# O desenvolvimento web em Python geralmente se divide em duas partes:
# 1. Front-end: O que o usuário vê (HTML, CSS, JavaScript).
# 2. Back-end: Onde a lógica e os dados são processados (Python/Flask).

# 1. DEMONSTRAÇÃO DE CONTEÚDO FRONT-END (HTML BÁSICO)
# O Python é usado aqui apenas para gerar a string que representa a página.
html_basico = """
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo de Front-end com Python</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Esta é uma estrutura HTML básica para demonstração.</p>
</body>
</html>
"""

print("--- 1. Estrutura HTML Simples ---")
print(html_basico)


# 2. DEMONSTRAÇÃO DE BACK-END (ESTRUTURA FLASK)
# Este código demonstra a estrutura de um servidor Flask.
# Para rodar, seria necessário instalar as bibliotecas e usar um túnel (ex: ngrok).
def estrutura_backend_flask():
    """
    Simulação da estrutura mínima de um servidor Flask.
    """
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        # Retorna o conteúdo que o back-end envia para o front-end
        return 'Olá, esta é a rota principal do back-end!'

    # if __name__ == '__main__':
    #     app.run()
    
    print("\n--- 2. Estrutura de Back-end com Flask (Rota Principal) ---")
    print("Definida a função 'index()' que atende à rota '/'")

estrutura_backend_flask()
