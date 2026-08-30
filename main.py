with open("main.py", "w") as f:
    f.write('''
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.utils import platform

class MenuPanel(BoxLayout):
    """Бічна панель навігації, як в оригінальній ПК-версії"""
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_x = 0.25
        self.spacing = 5
        self.padding = 5
        
        self.add_widget(Label(text="БЗВП\nРОЗКЛАД", font_size='16sp', bold=True, size_hint_y=None, height=50, halign='center'))
        
        # Кнопки лівого меню
        btn_shabloni = Button(text="📋 Шаблони", size_hint_y=None, height=45)
        btn_algoritmi = Button(text="⚙️ Алгоритми", size_hint_y=None, height=45)
        btn_import = Button(text="📥 Імпорт JSON", size_hint_y=None, height=45)
        
        btn_shabloni.bind(on_press=lambda x: setattr(sm, 'current', 'shabloni'))
        btn_algoritmi.bind(on_press=lambda x: setattr(sm, 'current', 'algoritmi'))
        btn_import.bind(on_press=lambda x: setattr(sm, 'current', 'import'))
        
        self.add_widget(btn_shabloni)
        self.add_widget(btn_algoritmi)
        self.add_widget(btn_import)
        self.add_widget(Label()) # Розпірка

class ImportScreen(Screen):
    """Екран завантаження JSON-структури"""
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app = app_instance
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Вставте текст вашого JSON шаблону сюди:", font_size='16sp', size_hint_y=None, height=30))
        
        self.json_input = TextInput(hint_text='{"exportedAt": "2026...", "templates": [...]}', multiline=True)
        layout.add_widget(self.json_input)
        
        import_btn = Button(text="Імпортувати дані", background_color=(0.1, 0.5, 0.1, 1), size_hint_y=None, height=50)
        import_btn.bind(on_press=self.process_import)
        layout.add_widget(import_btn)
        
        self.status_lbl = Label(text="", size_hint_y=None, height=30)
        layout.add_widget(self.status_lbl)
        
        self.add_widget(layout)

    def process_import(self, instance):
        try:
            raw_data = self.json_input.text.strip()
            parsed = json.loads(raw_data)
            self.app.game_data = parsed
            self.status_lbl.text = "[color=00FF00]Імпорт успішний! Дані завантажено.[/color]"
            self.status_lbl.markup = True
        except Exception as e:
            self.status_lbl.text = f"[color=FF0000]Помилка імпорту: {str(e)}[/color]"
            self.status_lbl.markup = True

class ShabloniScreen(Screen):
    """Екран відображення мобільних карток Шаблонів"""
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app = app_instance

    def on_pre_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="Навчальні Шаблони БЗВП", font_size='20sp', bold=True, size_hint_y=None, height=40))
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        templates = self.app.game_data.get("templates", [])
        if not templates:
            grid.add_widget(Label(text="Немає завантажених шаблонів. Перейдіть в Імпорт.", font_size='14sp'))
        else:
            for t in templates:
                row = BoxLayout(orientation='vertical', size_hint_y=None, height=80, padding=10, spacing=5)
                row.add_widget(Label(text=f"📌 Назва: {t.get('name', 'Без назви')}", font_size='16sp', bold=True, halign='left'))
                row.add_widget(Label(text=f"Кількість занять в базі: {len(t.get('templateItems', []))}", font_size='14sp', color=(0.7,0.7,0.7,1)))
                grid.add_widget(row)
                
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

class AlgoritmiScreen(Screen):
    """Екран відображення Алгоритмів підрозділів"""
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app = app_instance

    def on_pre_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="Робочі Алгоритми", font_size='20sp', bold=True, size_hint_y=None, height=40))
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        algorithms = self.app.game_data.get("algorithms", [])
        if not algorithms:
            grid.add_widget(Label(text="Немає активних алгоритмів.", font_size='14sp'))
        else:
            for alg in algorithms:
                status_color = "[color=3399FF]" if alg.get('status') == "Published" else "[color=999999]"
                info_text = f"⚙️ {alg.get('name')} ({alg.get('subUnit')})\nПериод: {alg.get('startDate')} - {alg.get('endDate')} | {status_color}{alg.get('status')}[/color]"
                
                lbl = Label(text=info_text, markup=True, font_size='14sp', size_hint_y=None, height=60, halign='left')
                lbl.bind(size=lbl.setter('text_size'))
                grid.add_widget(lbl)
                
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

class MainLayout(BoxLayout):
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        
        sm = ScreenManager()
        sm.add_widget(ShabloniScreen(app_instance, name='shabloni'))
        sm.add_widget(AlgoritmiScreen(app_instance, name='algoritmi'))
        sm.add_widget(ImportScreen(app_instance, name='import'))
        
        self.add_widget(MenuPanel(sm=sm))
        self.add_widget(sm)

class ScheduleCloneApp(App):
    def build(self):
        # Початковий пустий словник, який заповниться при імпорті
        self.game_data = {"templates": [], "algorithms": []}
        return MainLayout(self)

if __name__ == '__main__':
    ScheduleCloneApp().run()
''')
print("Повноцінний мобільний клон БЗВП успішно згенеровано у файл main.py!")
