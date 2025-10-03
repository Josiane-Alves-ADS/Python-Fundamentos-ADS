# --- APLICAÇÃO COMPLETA: CALCULADORA KIVYMD ---
# Este script demonstra como ligar a interface (KV) à lógica (Python)
# em um ambiente KivyMD, criando um aplicativo funcional.

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

# Nota: O código foi corrigido em relação aos erros de sintaxe (como f-strings incompletas e blocos try/except abertos).

# 1. Definição da Interface (KV Language)
KV_CALC = '''
<CalculatorApp>:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)

    # Campo de Entrada/Resultado
    MDTextField:
        id: input_field
        hint_text: "0"
        mode: "rectangle"
        font_size: '30sp'
        halign: 'right'
        readonly: True

    # Grid de Botões
    GridLayout:
        cols: 4
        spacing: dp(10)

        # Primeira Linha
        MDRaisedButton:
            text: "C"
            on_press: app.clear_input()
            md_bg_color: 0.8, 0.1, 0.1, 1 # Vermelho para Clear
        MDRaisedButton:
            text: "7"
            on_press: app.on_number_press(7)
        MDRaisedButton:
            text: "8"
            on_press: app.on_number_press(8)
        MDRaisedButton:
            text: "/"
            on_press: app.on_operator_press("/")
            md_bg_color: 0.1, 0.5, 0.8, 1 # Azul para Operadores

        # Segunda Linha
        MDRaisedButton:
            text: "4"
            on_press: app.on_number_press(4)
        MDRaisedButton:
            text: "5"
            on_press: app.on_number_press(5)
        MDRaisedButton:
            text: "6"
            on_press: app.on_number_press(6)
        MDRaisedButton:
            text: "*"
            on_press: app.on_operator_press("*")
            md_bg_color: 0.1, 0.5, 0.8, 1

        # Terceira Linha
        MDRaisedButton:
            text: "1"
            on_press: app.on_number_press(1)
        MDRaisedButton:
            text: "2"
            on_press: app.on_number_press(2)
        MDRaisedButton:
            text: "3"
            on_press: app.on_number_press(3)
        MDRaisedButton:
            text: "-"
            on_press: app.on_operator_press("-")
            md_bg_color: 0.1, 0.5, 0.8, 1

        # Quarta Linha
        MDRaisedButton:
            text: "0"
            on_press: app.on_number_press(0)
        MDRaisedButton:
            text: "."
            on_press: app.on_number_press(".")
        MDRaisedButton:
            text: "="
            on_press: app.calculate_result()
            md_bg_color: 0.1, 0.8, 0.5, 1 # Verde para Igual
        MDRaisedButton:
            text: "+"
            on_press: app.on_operator_press("+")
            md_bg_color: 0.1, 0.5, 0.8, 1
'''

# 2. Lógica do Aplicativo (Python Class)
class CalculatorApp(BoxLayout):
    """Classe do Layout/Widget que contém a lógica da calculadora."""

    # Corrigindo a inserção de números
    def on_number_press(self, number):
        current_text = self.ids.input_field.text
        # Permite adicionar ponto decimal, mas apenas se não houver um no número atual
        if number == '.' and (not current_text or current_text[-1] in '+-*/ ' or '.' in current_text.split()[-1]):
             # Evita adicionar ponto se o último token já tiver um
            pass
        elif current_text == '0':
            self.ids.input_field.text = str(number)
        else:
            self.ids.input_field.text = current_text + str(number)

    # Corrigindo a inserção de operadores
    def on_operator_press(self, operator):
        current_text = self.ids.input_field.text
        if current_text and current_text[-1] not in '+-*/ ':
            self.ids.input_field.text = f"{current_text} {operator} "

    def clear_input(self):
        self.ids.input_field.text = "0" # Limpa o campo

    def calculate_result(self):
        try:
            # Usa eval para calcular a expressão. Em produção, isso seria inseguro.
            result = eval(self.ids.input_field.text)
            self.ids.input_field.text = str(result)
        except Exception:
            self.ids.input_field.text = "Erro" # Trata erros de expressão


# 3. Classe Principal do App KivyMD
class CalculatorMDApp(MDApp):
    def build(self):
        # O Builder deve carregar o KV antes de tentar acessar 'CalculatorApp'
        Builder.load_string(KV_CALC)
        return CalculatorApp()

    # Redireciona os eventos dos botões (on_press: app.metodo) para a instância raiz (self.root)
    def on_number_press(self, number):
        self.root.on_number_press(number)
    def on_operator_press(self, operator):
        self.root.on_operator_press(operator)
    def clear_input(self):
        self.root.clear_input()
    def calculate_result(self):
        self.root.calculate_result()

if __name__ == '__main__':
    # CalculatorMDApp().run()
    print("Módulo KivyMD: Demonstração de Aplicativo Calculadora funcional carregado.")
