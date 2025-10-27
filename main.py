import flet as ft
import datetime
from db import main_db

def main(page: ft.Page):
    page.title = 'ToDo list'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)

    def load_task():
        task_list.controls.clear()
        for task_id, task_text, is_completed in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id=task_id, task_text=task_text, is_completed=is_completed))
        page.update()

    def create_task_row(task_id, task_text, is_completed):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        task_time = ft.Text(value=time)

        def enable_edit(_):
            task_field.read_only = False
            task_field.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, tooltip="Редактировать", on_click=enable_edit, icon_color=ft.Colors.ORANGE_700)

        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            task_field.update()
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE_ALT_ROUNDED, on_click=save_task)

        def delete_task(_):
            main_db.delete_task(task_id=task_id)
            load_task()

        delete_button = ft.IconButton(icon=ft.Icons.DELETE, tooltip="Удалить", on_click=delete_task, icon_color=ft.Colors.RED_700)

        def toggle_complete(_):
            if is_completed == 0:
                main_db.mark_task_as_completed(task_id)
            else:
                main_db.mark_task_as_completed(task_id)  # Измените на функционал для отмены

            load_task()

        complete_button = ft.IconButton(
            icon=ft.Icons.CHECK, tooltip="Отметить как выполненную", on_click=toggle_complete,
            icon_color=ft.Colors.GREEN_700 if is_completed == 0 else ft.Colors.GRAY_400
        )

        return ft.Row([task_time, task_field, edit_button, save_button, delete_button, complete_button])

    def add_task(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task)
            task_list.controls.append(create_task_row(task_id=task_id, task_text=task, is_completed=0))

            task_input.value = ''
            page.update()

    def delete_completed_tasks(_):
        main_db.delete_completed_tasks()
        load_task()

    task_input = ft.TextField(label='Введите новую задачу', expand=True)
    add_button = ft.IconButton(icon=ft.Icons.ADD, tooltip='Добавить задачу', on_click=add_task)
    delete_all_button = ft.ElevatedButton(text='Удалить все выполненные', on_click=delete_completed_tasks)

    page.add(ft.Row([task_input, add_button, delete_all_button]), task_list)

    load_task()

if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)
