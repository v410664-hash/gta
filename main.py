from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BulldozerAppUI(BoxLayout):
    def __init__(self, **kwargs):
        super(BulldozerAppUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # Заголовок
        self.add_widget(Label(
            text='Мій APK додаток',
            font_size=24,
            size_hint_y=None,
            height=50
        ))

        # Поле введення
        self.user_input = TextInput(
            text='',
            hint_text='Введіть текст тут...',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.user_input)

        # Кнопка
        self.submit_btn = Button(
            text='Натисни мене',
            size_hint_y=None,
            height=60
        )
        self.submit_btn.bind(on_press=self.on_button_click)
        self.add_widget(self.submit_btn)

        # Вивід результату
        self.output_label = Label(
            text='Результат з'явиться тут',
            font_size=18
        )
        self.add_widget(self.output_label)

    def on_button_click(self, instance):
        text = self.user_input.text
        if text:
            self.output_label.text = f'Привіт, {text}!'
        else:
            self.output_label.text = 'Ви нічого не ввели!'

class MainApp(App):
    def build(self):
        return BulldozerAppUI()

if __name__ == '__main__':
    MainApp().run()
