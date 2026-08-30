import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


class MenuPanel(BoxLayout):

  def __init__(self, sm, **kwargs):
    super().__init__(**kwargs)
    self.orientation = "vertical"
    self.size_hint_x = 0.3
    self.spacing = 5
    self.padding = 5

    title = Label(
        text="БЗВП\nРОЗКЛАД",
        font_size="16sp",
        bold=True,
        size_hint_y=None,
        height=60,
        halign="center",
    )
    title.bind(size=lambda instance, value: setattr(instance, "text_size", value))
    self.add_widget(title)

    btn_shabloni = Button(text="📋 Шаблони", size_hint_y=None, height=45)
    btn_algoritmi = Button(text="⚙️ Алгоритми", size_hint_y=None, height=45)
    btn_import = Button(text="📥 Імпорт JSON", size_hint_y=None, height=45)

    btn_shabloni.bind(on_press=lambda x: setattr(sm, "current", "shabloni"))
    btn_algoritmi.bind(on_press=lambda x: setattr(sm, "current", "algoritmi"))
    btn_import.bind(on_press=lambda x: setattr(sm, "current", "import"))

    self.add_widget(btn_shabloni)
    self.add_widget(btn_algoritmi)
    self.add_widget(btn_import)
    self.add_widget(Label())


class ImportScreen(Screen):

  def __init__(self, app_instance, **kwargs):
    super().__init__(**kwargs)
    self.app = app_instance
    layout = BoxLayout(orientation="vertical", padding=15, spacing=10)

    title = Label(
        text="Вставте текст вашого JSON шаблону сюди:",
        font_size="16sp",
        size_hint_y=None,
        height=30,
        halign="left",
    )
    title.bind(size=lambda instance, value: setattr(instance, "text_size", value))
    layout.add_widget(title)

    self.json_input = TextInput(
        hint_text='{"templates": [...], "algorithms": [...]}', multiline=True
    )
    layout.add_widget(self.json_input)

    import_btn = Button(
        text="Імпортувати дані",
        background_color=(0.1, 0.6, 0.2, 1),
        size_hint_y=None,
        height=50,
        bold=True,
    )
    import_btn.bind(on_press=self.process_import)
    layout.add_widget(import_btn)

    self.status_lbl = Label(size_hint_y=None, height=40, markup=True)
    layout.add_widget(self.status_lbl)
    self.add_widget(layout)

  def process_import(self, instance):
    try:
      raw_data = self.json_input.text.strip()
      parsed = json.loads(raw_data)
      self.app.game_data = parsed
      self.app.save_local_data()
      self.status_lbl.text = (
          "[color=00FF00]Успішно! Дані імпортовано та збережено.[/color]"
      )
    except Exception as e:
      self.status_lbl.text = f"[color=FF0000]Помилка імпорту: {str(e)}[/color]"


class ShabloniScreen(Screen):

  def __init__(self, app_instance, **kwargs):
    super().__init__(**kwargs)
    self.app = app_instance

  def on_pre_enter(self):
    self.clear_widgets()
    layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
    layout.add_widget(
        Label(
            text="Навчальні Шаблони БЗВП",
            font_size="20sp",
            bold=True,
            size_hint_y=None,
            height=40,
        )
    )

    scroll = ScrollView()
    grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
    grid.bind(minimum_height=grid.setter("height"))

    templates = self.app.game_data.get("templates", [])
    if not templates:
      grid.add_widget(
          Label(
              text="Немає завантажених шаблонів.\nПерейдіть в Імпорт JSON.",
              font_size="14sp",
              halign="center",
          )
      )
    else:
      for t in templates:
        row = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=70,
            padding=5,
            spacing=2,
        )

        lbl_title = Label(
            text=f"📌 Назва: {t.get('name', 'Без назви')}",
            font_size="16sp",
            bold=True,
            halign="left",
        )
        lbl_title.bind(
            size=lambda instance, value: setattr(instance, "text_size", value)
        )

        lbl_items = Label(
            text=f"Занять у базі: {len(t.get('templateItems', []))}",
            font_size="13sp",
            color=(0.7, 0.7, 0.7, 1),
            halign="left",
        )
        lbl_items.bind(
            size=lambda instance, value: setattr(instance, "text_size", value)
        )

        row.add_widget(lbl_title)
        row.add_widget(lbl_items)
        grid.add_widget(row)

    scroll.add_widget(grid)
    layout.add_widget(scroll)
    self.add_widget(layout)


class AlgoritmiScreen(Screen):

  def __init__(self, app_instance, **kwargs):
    super().__init__(**kwargs)
    self.app = app_instance

  def on_pre_enter(self):
    self.clear_widgets()
    layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
    layout.add_widget(
        Label(
            text="Робочі Алгоритми",
            font_size="20sp",
            bold=True,
            size_hint_y=None,
            height=40,
        )
    )

    scroll = ScrollView()
    grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
    grid.bind(minimum_height=grid.setter("height"))

    algorithms = self.app.game_data.get("algorithms", [])
    if not algorithms:
      grid.add_widget(
          Label(text="Немає активних алгоритмів.", font_size="14sp")
      )
    else:
      for alg in algorithms:
        status_color = (
            "[color=3399FF]"
            if alg.get("status") == "Published"
            else "[color=999999]"
        )
        info_text = (
            f"⚙️ {alg.get('name')} ({alg.get('subUnit', '—')})\nПеріод:"
            f" {alg.get('startDate', '')} - {alg.get('endDate', '')} |"
            f" {status_color}{alg.get('status', '')}[/color]"
        )
        lbl = Label(
            text=info_text,
            markup=True,
            font_size="14sp",
            size_hint_y=None,
            height=60,
            halign="left",
        )
        lbl.bind(
            size=lambda instance, value: setattr(instance, "text_size", value)
        )
        grid.add_widget(lbl)

    scroll.add_widget(grid)
    layout.add_widget(scroll)
    self.add_widget(layout)


class MainLayout(BoxLayout):

  def __init__(self, app_instance, **kwargs):
    super().__init__(**kwargs)
    self.orientation = "horizontal"
    sm = ScreenManager()
    sm.add_widget(ShabloniScreen(app_instance, name="shabloni"))
    sm.add_widget(AlgoritmiScreen(app_instance, name="algoritmi"))
    sm.add_widget(ImportScreen(app_instance, name="import"))
    self.add_widget(MenuPanel(sm=sm))
    self.add_widget(sm)


class ScheduleCloneApp(App):

  def build(self):
    self.data_filepath = os.path.join(self.user_data_dir, "schedule_data.json")
    self.load_local_data()
    return MainLayout(self)

  def load_local_data(self):
    if os.path.exists(self.data_filepath):
      try:
        with open(self.data_filepath, "r", encoding="utf-8") as f:
          self.game_data = json.load(f)
      except Exception:
        self.game_data = {"templates": [], "algorithms": []}
    else:
      self.game_data = {"templates": [], "algorithms": []}

  def save_local_data(self):
    try:
      with open(self.data_filepath, "w", encoding="utf-8") as f:
        json.dump(self.game_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
      print(f"Помилка збереження файлу: {e}")


if __name__ == "__main__":
  ScheduleCloneApp().run()
