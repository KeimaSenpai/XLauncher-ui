import flet as ft
# import logging

from views.home import create_home_page
from views.user import user_page
from views.new import new_page
from views.install import install_page
from views.setting import create_setting_page

# logging.basicConfig(level=logging.DEBUG)

def main(page: ft.Page):
    page.title = "XLauncher"
    page.window.width = 769
    page.window.height = 500
    page.window.resizable = False
    page.window.maximizable = False
    page.padding = 0
    page.theme_mode = "dark"
    page.fonts = {
        "mine": "fonts/minecraft.ttf",
        "mine_dun": "fonts/minecraft-dungeons.ttf",
        "nunito": "fonts/nunito-variablefont.ttf"
    }
    page.theme = ft.Theme(font_family="mine_dun")

    logo = ft.Container(
        content=ft.Image(src="img/logo.webp", height=45, width=45),
        alignment=ft.alignment.center,
        height=47,
        margin=10,
    )

    a = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda _: page.go("/"),
    )
    b = ft.IconButton(
        icon=ft.Icons.ACCOUNT_CIRCLE,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda _: page.go("/user"),
    )
    c = ft.IconButton(
        icon=ft.Icons.NEWSPAPER_OUTLINED,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda _: page.go("/new"),
    )
    d = ft.IconButton(
        icon=ft.Icons.DOWNLOAD,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda _: page.go("/install"),
    )
    e = ft.IconButton(
        icon=ft.Icons.SETTINGS,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda _: page.go("/setting"),
    )



    iconos = ft.Column(controls=[a, b, c, d, e,])

    # Navegación principal de la app
    nab = ft.Container(
        content=ft.Column(
            spacing=100,
            controls=[logo, iconos],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        height=478,
        width=70,
        bgcolor="#131313",
        alignment=ft.alignment.center,
    )



    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        spacing=0,
                        controls=[
                            nab,
                            create_home_page(page),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                padding=0,
            )
        )
        if page.route == "/user":
            page.views.append(
                ft.View(
                    "/user",
                    [
                        ft.Row(
                            spacing=0,
                            controls=[
                                nab,
                                user_page,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    padding=0,
                )
            )
        if page.route == "/new":
            page.views.append(
                ft.View(
                    "/new",
                    [
                        ft.Row(
                            spacing=0,
                            controls=[
                                nab,
                                new_page,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    padding=0,
                )
            )
        if page.route == "/install":
            page.views.append(
                ft.View(
                    "/install",
                    [
                        ft.Row(
                            spacing=0,
                            controls=[
                                nab,
                                install_page,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    padding=0,
                )
            )
        if page.route == "/setting":
            page.views.append(
                ft.View(
                    "/setting",
                    [
                        ft.Row(
                            spacing=0,
                            controls=[
                                nab,
                                create_setting_page(page),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    padding=0,
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="assets")
