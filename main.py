from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    def __init__(self, tarefas):
        super().__init__()
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))

class Test(App):
    def build(self):
        return Tarefas(['Fazer compras','Buscar filho'])

Test().run()