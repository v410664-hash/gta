import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import QLabel
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView

DATA_FILE = "bzvp_schedule.json"

class ScheduleApp(App):
    def build(self):
        self.title = "Конструктор розкладу БЗВП"
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = QLabel(text="Графічний розклад занять", font_size=20, size_hint=(1, 0.08), bold=True)
        main_layout.add_widget(header)
        
        # Таблиця з прокручуванням
        scroll = ScrollView(size_hint=(1, 0.77))
        self.grid = GridLayout(cols=4, spacing=5, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        
        scroll.add_widget(self.grid)
        main_layout.add_widget(scroll)
        
        # Панель кнопок
        btn_layout = BoxLayout(size_hint=(1, 0.15), spacing=5)
        
        btn_load = Button(text="📂 Відкрити JSON", background_color=(0.2, 0.6, 0.8, 1))
        btn_load.bind(on_press=self.open_file_chooser)
        btn_layout.add_widget(btn_load)
        
        btn_add = Button(text="+ Рядок", background_color=(0.1, 0.5, 0.8, 1))
        btn_add.bind(on_press=lambda x: self.add_row("", "", "", ""))
        btn_layout.add_widget(btn_add)
        
        btn_save = Button(text="💾 Зберегти", background_color=(0.1, 0.7, 0.2, 1))
        btn_save.bind(on_press=self.save_data)
        btn_layout.add_widget(btn_save)
        
        main_layout.add_widget(btn_layout)
        
        self.load_data_from_path(DATA_FILE)
        
        return main_layout

    def add_row(self, day, time, subject, location):
        """Додає новий рядок у таблицю"""
        t1 = TextInput(text=str(day), multiline=False, size_hint_y=None, height=40)
        t2 = TextInput(text=str(time), multiline=False, size_hint_y=None, height=40)
        t3 = TextInput(text=str(subject), multiline=False, size_hint_y=None, height=40)
        t4 = TextInput(text=str(location), multiline=False, size_hint_y=None, height=40)
        
        self.inputs.append((t1, t2, t3, t4))
        
        self.grid.add_widget(t1)
        self.grid.add_widget(t2)
        self.grid.add_widget(t3)
        self.grid.add_widget(t4)
        
        self.grid.height = (len(self.inputs) + 1) * 45

    def open_file_chooser(self, instance):
        """Вспливаюче вікно для вибору JSON файлу з пам'яті"""
        content = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView(path='/sdcard' if os.path.exists('/sdcard') else '.', filters=['*.json'])
        
        content.add_widget(file_chooser)
        
        btn_select = Button(text="Завантажити вибране", size_hint=(1, 0.15))
        content.add_widget(btn_select)
        
        popup = Popup(title="Оберіть JSON файл", content=content, size_hint=(0.9, 0.9))
        
        def select_file(btn_instance):
            if file_chooser.selection:
                selected_file = file_chooser.selection[0]
                self.load_data_from_path(selected_file)
                popup.dismiss()

        btn_select.bind(on_press=select_file)
        popup.open()

    def load_data_from_path(self, filepath):
        """Зчитує JSON файл за вказаним шляхом"""
        self.inputs = []
        self.grid.clear_widgets()
        
        # Шапка
        headers = ["День", "Час", "Дисципліна", "Місце"]
        for h in headers:
            self.grid.add_widget(QLabel(text=h, bold=True, size_hint_y=None, height=35))
        
        data = []
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception as e:
                print(f"Помилка читання: {e}")
        
        if not data:
            data = [
                {"day": "День 1", "time": "09:00 - 13:00", "subject": "Вогнева підготовка (ВП)", "location": "Тир"}
            ]
            
        for item in data:
            self.add_row(item.get("day", ""), item.get("time", ""), item.get("subject", ""), item.get("location", ""))

    def save_data(self, instance):
        """Зберігає таблицю у файл"""
        data = []
        for t1, t2, t3, t4 in self.inputs:
            data.append({
                "day": t1.text,
                "time": t2.text,
                "subject": t3.text,
                "location": t4.text
            })
            
        try:
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("Збережено успішно!")
        except Exception as e:
            print(f"Помилка збереження: {e}")

if __name__ == '__main__':
    ScheduleApp().run()
