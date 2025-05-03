import os
import flet as ft
import json
from minecraft_launcher.confi_env import RUTA_JSON
from minecraft_launcher.minecraft import latest_versions, save_config


# Verificar si el archivo de configuración existe y cargar datos si existe
if os.path.exists(RUTA_JSON):
    with open(RUTA_JSON, 'r') as file:
        config_data = json.load(file)
else:
    config_data = {
        "username": "",
        "uuid": "",
        "token": "",
        "ram": "",
        "version": "",
        "java": ""
    }

# Obtiene la lista de versiones instaladas
versions = latest_versions()
opciones = [ft.dropdown.Option(version) for version in versions]

title = ft.Text('Perfil', font_family='mine_dun', size=30)

username = ft.TextField(
    hint_text="User Name",
    width=250,
    height=50,
    bgcolor='#343434',
    border=ft.InputBorder.NONE,
    border_radius=30,
    cursor_height=20,
    text_style=ft.TextStyle(
        font_family='mine',
        size=15,
    ),
    value=config_data.get("username", "")
)

# Establecer un valor predeterminado para RAM
try:
    ram_default = float(config_data.get("ram"))
except (TypeError, ValueError):
    ram_default = 2  # Valor por defecto (modifícalo si lo deseas)

ram = ft.Slider(
        min=0, 
        max=12,
        active_color='#5B0098',
        # inactive_color='#ffffff',
        # thumb_color='#ffffff',
        # overlay_color='#fffff5',
        # secondary_active_color='#ffffff',

        divisions=6, 
        label="{value}", 
        value=ram_default,
    )

version = ft.Dropdown(
    width=250,
    bgcolor="#343434",
    border=ft.InputBorder.NONE,
    text_style=ft.TextStyle(
        font_family='mine',
        size=15,
    ),
    options=opciones,
    value=config_data.get("version", "")
)

guardar_btn = ft.ElevatedButton(
    "Guardar",
    style=ft.ButtonStyle(
        color="#ffffff",
        bgcolor="#5B0098",
        overlay_color="#0C0C0C",
        shape=ft.RoundedRectangleBorder(radius=3),
        shadow_color="#000000",
        elevation=5,
    ),
    on_click=lambda _: save_config(mine_user=username.value, ram=int(ram.value), version=version.value),
)

user_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[
                    title,
                    username,
                    ram,
                    version,
                    guardar_btn,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    ],
    width=681,
    height=478,
)