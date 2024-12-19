import flet as ft


def main(page: ft.Page):
    
    page.vertical_alignment = ft.VerticalAlignment.CENTER
    page.padding = 0
    
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            last_name = txt_last_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name} {last_name}!"))

    txt_name = ft.TextField(label="Введите ваше имя")
    txt_last_name = ft.TextField(label="Введите вашу фамилию")
    button = ft.ElevatedButton("Say hello!", on_click=btn_click)

    page.add(txt_name, button)


ft.app(main)
