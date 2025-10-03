# --- FRONT-END: PERFIL PROFISSIONAL COM CSS INLINE ---
# Demonstra a criação de uma página web mais complexa, estilizada usando CSS inline.
# Este é um ótimo exemplo de como estruturar uma página de portfólio simples.

html_perfil_profissional = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Perfil</title>
</head>
<body style="font-family: 'Arial', sans-serif; background-color: #f8f8f8; margin: 0; padding: 0;">

    <header style="text-align: center; background-color: #3498db; color: #fff; padding: 20px;">
        <h1 style="margin: 0;">Anderson Inácio Salata de Abreu</h1>
        <p style="margin: 5px 0;">Desenvolvedor Web</p>
    </header>

    <section style="margin: 20px; text-align: center;">
        <img src="content/sua_foto.jpg" alt="Sua Foto" style="border-radius: 50%; margin-bottom: 20px; width: 100px; height: 100px; object-fit: cover; border: 3px solid #3498db;">
        <div id="informacoes-pessoais" style="max-width: 400px; margin: 0 auto;">
            <p>Cidade: Sorocaba | País: Brasil</p>
            <p>Interesses: Web Development, Programação, etc.</p>
        </div>
    </section>

    <section style="margin: 20px; text-align: center; border-top: 1px solid #ddd; padding-top: 20px;">
        <h2>Habilidades</h2>
        <ul style="list-style: none; padding: 0;">
            <li style="margin-bottom: 5px;">Linguagens: Python, HTML, CSS, JavaScript</li>
            <li>Ferramentas: Git, VS Code</li>
        </ul>
    </section>

    <footer style="text-align: center; margin-top: 20px; padding: 20px; background-color: #eee;">
        <a href="https://www.linkedin.com/in/andersonsalata/" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;">LinkedIn</a>
    </footer>
</body>
</html>
"""

print("--- Demonstração de Perfil Profissional (HTML + CSS Inline) ---")
print("Este código simula um cartão de visita digital com informações estruturadas.")
# Para visualização em ambientes como o Colab, a linha abaixo seria usada:
# from IPython.display import HTML
# HTML(html_perfil_profissional)
