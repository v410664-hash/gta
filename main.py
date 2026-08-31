import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class ScheduleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(
            text='Конструктор розкладу БЗВП', 
            font_size='20sp', 
            size_hint_y=None, 
            height=50
        ))
        
        data_text = "Файл bzvp_schedule.json не знайдено."
        if os.path.exists('bzvp_schedule.json'):
            try:
                with open('bzvp_schedule.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    data_text = json.dumps(data, ensure_ascii=False, indent=2)
            except Exception as e:
                data_text = f"Помилка читання JSON: {e}"

        scroll = ScrollView()
        content_label = Label(
            text=data_text, 
            size_hint_y=None, 
            halign='left', 
            valign='top'
        )
        content_label.bind(
            texture_size=lambda instance, value: setattr(instance, 'height', value[1]),
            width=lambda instance, value: setattr(instance, 'text_size', (value, None))
        )
        scroll.add_widget(content_label)
        layout.add_widget(scroll)
        
        return layout

if __name__ == '__main__':
    ScheduleApp().run()
