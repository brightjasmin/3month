import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Приветствие с подсветкой имени"
    page.theme_mode = ft.ThemeMode.LIGHT

    name_input = ft.TextField(label="Введите ваше имя", width=320)
    greeting_text = ft.Text(spans=[])  # будет содержать TextSpan'ы

    def get_greeting_part() -> str:
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return "Доброе утро, "
        elif 12 <= hour < 18:
            return "Добрый день, "
        elif 18 <= hour < 24:
            return "Добрый вечер, "
        else:
            return "Доброй ночи, "

    def show_greeting(e):
        name = name_input.value.strip()
        if not name:
            # показываем snackbar вместо изменения текста
            page.snack_bar = ft.SnackBar(ft.Text("Введите имя!"))
            page.snack_bar.open = True
        else:
            greeting_text.spans = [
                ft.TextSpan(get_greeting_part()),
                # выделяем имя: жирный + синий (hex)
                ft.TextSpan(name, style=ft.TextStyle(weight="bold", color="#1E88E5")),
                ft.TextSpan("!")
            ]
        page.update()

    # Тема: иконка через content
    theme_button = ft.IconButton(content=ft.Icon(name="brightness_7"), tooltip="Сменить тему")

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.content = ft.Icon(name="brightness_2")
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.content = ft.Icon(name="brightness_7")
        page.update()

    theme_button.on_click = toggle_theme

    greet_button = ft.ElevatedButton("Поздороваться", on_click=show_greeting)

    page.add(
        ft.Row([theme_button], alignment=ft.MainAxisAlignment.END),
        name_input,
        greet_button,
        ft.Divider(),
        greeting_text,
    )

ft.app(target=main)
