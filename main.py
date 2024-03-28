import flet as ft
from flet import *


def main(page: ft.Page):
    page.title = "XLink"
    page.window_width = 715
    page.window_height = 450
    page.window_resizable = False
    page.padding = 0
    page.fonts = {
        "Revamped": "assets/fonts/minecraft-dungeons.ttf"
    }



    #Navegacion principal de la app
    nab = ft.Container(
        height= 450,
        width= 76,
        bgcolor='#329acc'
    )
    #Pagina inicial
    conte = ft.Container(
        height=450,
        width=639,
        bgcolor='#68c90e'

    )

    #Se agrupan todas las paginas
    page.add(
        ft.Row(spacing=0,
            controls=[
                nab,
                conte
            ]
        )
    )

ft.app(target=main, assets_dir='assets')