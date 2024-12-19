# import flet as ft


# def main(page: ft.Page):
#     page.title = "Кто хочет стать миллионером"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.bgcolor = "#000000"
#     # page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE_GREY)
#     # page.vertical_alignment = ft.VerticalAlignment.CENTER
#     # page.horizontal_alignment = ft.MainAxisAlignment.CENTER
#     page.padding = 0
    
#     def btn_click(e):
#         if not txt_login.value and not txt_password.value:
#             txt_login.error_text = "Логин обязательно"
#             txt_password.error_text = "Пароль обязательно"
#             page.update()
#         else:
#             login = txt_login.value
#             password = txt_password.value
#             page.clean()
#             page.add(ft.Text(f"Hello, {login} {password}!"))

#     txt_login = ft.TextField(label="Введите ваш логин", height=100)
#     txt_password = ft.TextField(label="Введите ваш пароль", height=100)
#     button = ft.Row([ft.ElevatedButton("Войти!", on_click=btn_click, bgcolor=ft.colors.INDIGO, color=ft.colors.WHITE)])
#     con = ft.Row([
#         ft.Container(
#         ft.Column([
#         txt_login,
#         txt_password,
#         button
#     ],alignment = ft.MainAxisAlignment.CENTER), bgcolor='#8e8e8e', padding=20, border_radius=20
#         )
#     ], alignment=ft.MainAxisAlignment.CENTER)
#     page.add(con)


# ft.app(main)



import flet as ft


def main(page: ft.Page):
    
    page.title = "Кто хочет стать миллионером"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#000000"
    
    def btn_click_reg(e):
        if not txt_login.value and not txt_password.value and not txt_name.value:
            txt_name.error_text = "Имя обязательно"
            txt_login.error_text = "Логин обязательно"
            txt_password.error_text = "Пароль обязательно"
            page.update()
        else:
            name = txt_name.value
            login = txt_login.value
            password = txt_password.value
            print(f"Hello, {login} {password} {name}!")
            page.clean()
            page.add(ft.Text(f"Hello, {login} {password}!"))
            
    def btn_click_log(e):
        if not txt_login.value and not txt_password.value:
            
            txt_login.error_text = "Логин обязательно"
            txt_password.error_text = "Пароль обязательно"
            page.update()
        else:
            
            login = txt_login.value
            password = txt_password.value
            page.clean()
            page.add(ft.Text(f"Hello, {login} {password}!"))
    
    
    txt_name = ft.TextField(label="Введите ваше имя", height=100)
    txt_login = ft.TextField(label="Введите ваш логин", height=100)
    txt_password = ft.TextField(label="Введите ваш пароль", height=100)
    button_reg = ft.Row([ft.ElevatedButton("Войти!", on_click=btn_click_reg, bgcolor=ft.colors.INDIGO, color=ft.colors.WHITE)])
    button_log = ft.Row([ft.ElevatedButton("Войти!", on_click=btn_click_log, bgcolor=ft.colors.INDIGO, color=ft.colors.WHITE)])
    
    def route_change(e):
        page.views.clear()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.bgcolor = "#000000"
        page.views.append(
            ft.View(
                "/login",
                [
                    # AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT),
                    ft.Row([
                            ft.Container(
                            ft.Column([
                            txt_login,
                            txt_password,
                            ft.Row([button_log, ft.ElevatedButton("Зарегистрироваться", on_click=lambda _: page.go("/register"))])
                        ],alignment = ft.MainAxisAlignment.CENTER), bgcolor='#8e8e8e', padding=20, border_radius=20
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER),
                ],
            )
        )
        if page.route == "/register":
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            page.bgcolor = "#000000"
            page.views.append(
                ft.View(
                    "/register",
                    [
                        # AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                        ft.Row([
                            ft.Container(
                            ft.Column([
                            txt_name, 
                            txt_login,
                            txt_password,
                            ft.Row([button_reg, ft.ElevatedButton("Есть аккаунт", on_click=lambda _: page.go("/login"))])
                        ],alignment = ft.MainAxisAlignment.CENTER), bgcolor='#8e8e8e', padding=20, border_radius=20
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        
                    ],
                )
            )
            
            
        if page.route == "/game":
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            page.bgcolor = "#000000"
            page.views.append(
                ft.View(
                    "/game",
                    [
                        # AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                        
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/login")),
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(main)
