# --- PROGRAMAÇÃO MOBILE COM KIVY/KIVYMD: LAYOUTS BÁSICOS ---
# O Kivy/KivyMD utiliza o conceito de classes Python e um DSL (Domain Specific Language)
# chamado KV para definir a interface.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
# Nota: Para rodar, você precisaria de 'pip install kivy kivymd'

# 1. Definição da Interface (KV Language)
KV_TABS = '''
<TabsLayout>:
    TabbedPanel:
        do_default_tab: False  # Remove a aba padrão
        tab_pos: 'top_mid'     # Posição das abas

        # Primeira Aba
        TabbedPanelItem:
            text: 'Dados'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Conteúdo da Aba de Dados'
                    font_size: '20dp'
                    color: (0.1, 0.5, 0.8, 1) # Cor azul

        # Segunda Aba
        TabbedPanelItem:
            text: 'Config'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Aba de Configurações'
                    font_size: '20dp'
                    color: (0.8, 0.5, 0.1, 1) # Cor laranja
'''

# 2. Classe Principal do Layout
class TabsLayout(BoxLayout):
    """Container para o TabbedPanel."""
    pass

# 3. Classe do Aplicativo
class TabsApp(App):
    def build(self):
        # Carrega a string KV antes de retornar o layout
        Builder.load_string(KV_TABS)
        return TabsLayout()

if __name__ == '__main__':
    # TabsApp().run()
    print("Módulo KivyMD: Demonstração de Layout com Abas (TabbedPanel) carregado.")
    print("Para rodar o app, descomente 'TabsApp().run()' e use um ambiente Kivy.")
