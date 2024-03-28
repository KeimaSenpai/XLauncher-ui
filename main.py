import flet as ft



def main(page: ft.Page):
    page.title = "XLink"
    page.window_width = 715
    page.window_height = 450
    page.window_resizable = False
    page.padding = 0
    page.fonts = {
        "Revamped": "fonts/minecraft-dungeons.ttf"
    }

    logo = ft.Image(src='img/logo.webp')
    play = ft.CupertinoFilledButton(
            content=ft.Text("CupertinoFilled"),
            opacity_on_click=0.3,
            on_click=lambda e: print("CupertinoFilledButton clicked!"),
        )
    nabvar = ft.Column(
        controls=[
            play
        ]
    )

    #Navegacion principal de la app
    nab = ft.Container(
        height= 450,
        width= 76,
        bgcolor='#131313'
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