import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Приветствие по времени суток"
    page.theme_mode = ft.ThemeMode.LIGHT  # начальная тема

    name_input = ft.TextField(label="Введите ваше имя", width=320)
    greeting_text = ft.Text("", size=20)  # обычный текст для вывода

    def get_greeting(name: str) -> str:
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= hour < 18:
            return f"Добрый день, {name}!"
        elif 18 <= hour < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"

    def show_greeting(e):
        name = name_input.value.strip() or "Гость"
        greeting_text.value = get_greeting(name)
        page.update()

    # Создаём IconButton, передаём иконку через content=ft.Icon(...)
    theme_button = ft.IconButton(content=ft.Icon(name="brightness_7"), tooltip="Сменить тему")

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            # обновим иконку на "луну"
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
        ft.Row([greet_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        greeting_text,
    )

ft.app(target=main)
