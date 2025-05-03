import flet as ft

from minecraft_launcher.minecraft import play_mine

def create_home_page(page):
    
    minecraft_title = ft.Image(
        src="img/minecraft_title.webp",
        height=170,
    )

    play = ft.ElevatedButton(
        "PLAY",
        width=100,
        style=ft.ButtonStyle(
            color="#ffffff",
            bgcolor="#5B0098",
            overlay_color="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=3),
            shadow_color="#000000",
            elevation=5,
            padding=10,
        ),
        on_click=play_mine,
    )

    home_page = ft.Stack(
        [
            ft.Image(
                src="img/bg.webp",
                height=478,
                width=681,
                fit=ft.ImageFit.COVER,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[minecraft_title, play],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
            ),
        ],
        width=681,
        height=478,
    )

    return home_page
