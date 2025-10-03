# --- FRONT-END AVANÇADO: HTML, CSS E INTERAÇÃO BÁSICA ---

# Demonstra um HTML com estilos CSS embutidos e um script JavaScript simples.
html_interativo_estilizado = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Web Estilizada</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f8f8;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            padding: 40px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
        }

        h1 {
            color: #3498db;
        }

        button {
            background-color: #3498db;
            color: #fff;
            font-size: 1.2em;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Olá, Mundo!</h1>
        <p>Esta página demonstra a integração de HTML, CSS e um pouco de JS.</p>
        <button onclick="console.log('Botão Clicado!')">Clique em Mim</button>
    </div>
</body>
</html>
"""

print("--- HTML com CSS e JavaScript (Interação) ---")
print("Este código gera uma página com estilo e um botão que registra um evento.")
# Normalmente, a linha abaixo seria executada:
# HTML(html_interativo_estilizado)
