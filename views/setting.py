import flet as ft
import json
import os

from minecraft_launcher.confi_env import LAUNCHER_VERSION, MINECRAFT_DIRECTORY, RUTA_JSON
from minecraft_launcher.minecraft import enviar_report


# Valores predeterminados para el archivo de configuración
default_config = {
    "username": "",
    "uuid": "",
    "token": "",
    "ram": "",
    "version": "",
    "java": ""
}

# Verificar si la carpeta existe, de lo contrario crearla
if not os.path.exists(MINECRAFT_DIRECTORY):
    os.makedirs(MINECRAFT_DIRECTORY)

# Verificar si el archivo existe, de lo contrario crearlo con los valores predeterminados
if not os.path.exists(RUTA_JSON):
    with open(RUTA_JSON, "w") as file:
        json.dump(default_config, file, indent=4)  # Escribir los valores iniciales con formato

# Cargar el archivo de configuración existente
with open(RUTA_JSON, "r") as file:
    config = json.load(file)


title = ft.Text("Ajustes", font_family="mine_dun", size=30)

def file_picker_result(e: ft.FilePickerResultEvent):
    if e.files:
        selected_path = e.files[0].path

        # Cargar la configuración actual del archivo JSON
        if os.path.exists(RUTA_JSON):
            with open(RUTA_JSON, "r") as file:
                config = json.load(file)  # Cargar el contenido actual del archivo

        # Actualizar solo el valor de "java"
        config["java"] = selected_path

        # Guardar la configuración actualizada
        with open(RUTA_JSON, "w") as file:
            json.dump(config, file, indent=4)  # Guardar sin afectar otros valores

        # Actualizar la interfaz de usuario
        java_path_text.value = selected_path
        java_path_text.update()


# Crear el FilePicker
file_picker = ft.FilePicker(on_result=file_picker_result)

# Mostrar la ruta del Java actual
java_path_text = ft.Text(config.get("java", ""), size=15, font_family='mine')


# Botón para seleccionar el Java
select_java_button = ft.ElevatedButton(
    text="Java",
    style=ft.ButtonStyle(
        color="#ffffff",
        bgcolor="#5B0098",
        overlay_color="#0C0C0C",
        shape=ft.RoundedRectangleBorder(radius=3),
        shadow_color="#000000",
        elevation=5,
    ),
    on_click=lambda _: file_picker.pick_files(dialog_title='Selecciona el Java', allowed_extensions=['exe'], initial_directory=MINECRAFT_DIRECTORY)
)



def create_setting_page(page):
    info_button = ft.IconButton(
        icon=ft.Icons.INFO,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda e: page.open(dlg)
    )

    info_text = ''' 
Launcher de Minecraft creado por Keima Senpai. El 
cual tiene el propósito de facilitar la instalación 
de Forge y Fabric. Además de tener una gran facilidad
de personalización.

'''

    dlg = ft.AlertDialog(
        title=ft.Text(
            f"XLauncher v{LAUNCHER_VERSION}", 
            font_family='mine',
            size=15,
            ),
        content=ft.Column(
            spacing = 5,
            controls=[
                ft.Image(src='img/logo_info.png', height=70),
                ft.Text(info_text, font_family='mine',size=12,),
                ft.Row(
                    spacing = 4,
                    controls=[
                        ft.IconButton(
                        content=ft.Image(src='img/telegram.png', height=30, width=30),
                        style=ft.ButtonStyle(
                            color="#5B0098",
                            bgcolor="#0C0C0C",
                            shape=ft.RoundedRectangleBorder(radius=5),
                        ),
                        on_click=lambda _: page.launch_url("https://t.me/+AfWKISuW0gRlMDQ5"),
                        
                    ),
                        ft.IconButton(
                        content=ft.Image(src='img/github.png', height=30, width=30),
                        style=ft.ButtonStyle(
                            color="#5B0098",
                            bgcolor="#0C0C0C",
                            shape=ft.RoundedRectangleBorder(radius=5),
                        ),
                        on_click=lambda _: page.launch_url("https://github.com/KeimaSenpai/XLauncher-ui"),
                        
                    ),
                        ft.IconButton(
                        content=ft.Image(src='img/youtube.png', height=30, width=30),
                        style=ft.ButtonStyle(
                            color="#5B0098",
                            bgcolor="#0C0C0C",
                            shape=ft.RoundedRectangleBorder(radius=5),
                        ),
                        on_click=lambda _: page.launch_url("https://www.youtube.com/@KeimaSenpaiYT"),
                        
                    ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(
                    disabled=False,
                    spans=[
                        ft.TextSpan('Copyright © 2025.  ',
                                    ft.TextStyle(
                                        font_family='mine',
                                    )
                                ),
                        ft.TextSpan('KeimaSenpai.  ', 
                                    ft.TextStyle(
                                        font_family='mine',
                                    ),
                                    url="https://github.com/KeimaSenpai",
                                ),
                        ft.TextSpan('LICENSE', 
                                    ft.TextStyle(
                                        font_family='mine',
                                    ),
                                    url="https://github.com/KeimaSenpai/XLauncher-ui/blob/main/LICENSE",
                                ),
                    ]
                )

            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        ),
        shape= ft.RoundedRectangleBorder(radius=5),
    )

    #Sección de reportes, bug, etc
    report_button = ft.IconButton(
        icon=ft.Icons.WARNING,
        style=ft.ButtonStyle(
            color="#e61a23",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda e: page.open(dlf)
    )

    contenedor = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Ruta del Java", size=15, font_family='mine'),
                ft.Column(
                    controls=[
                        java_path_text,
                        ft.Row(
                            controls=[
                                select_java_button,
                                report_button,
                                info_button
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
    )

    suport_category = ft.Dropdown(
        width=200,
        bgcolor="#343434",
        border=ft.InputBorder.NONE,
        options=[
            ft.dropdown.Option("Bug"),
            ft.dropdown.Option("Report"),
            ft.dropdown.Option("Sugerir"),
        ],
        text_style= ft.TextStyle(
            font_family='nunito',
            weight= ft.FontWeight.BOLD,
        )
    )

    btn_send_report = ft.ElevatedButton(
        "Enviar",
        style=ft.ButtonStyle(
            color="#ffffff",
            bgcolor="#5B0098",
            overlay_color="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=3),
            shadow_color="#000000",
            elevation=5,
        ),
        on_click=lambda _: enviar_report(suport_category.value, suport_texto.value),
    )

    suport_texto = ft.TextField(
        width=250,
        height=50,
        bgcolor='#343434',
        multiline=True,
        border=ft.InputBorder.NONE,
        border_radius=30,
        cursor_height=20,
        text_style=ft.TextStyle(
            font_family='nunito',
            size=15,
            ),
    )

    dlf = ft.AlertDialog(
        title=ft.Text(
            "CONTACTO", 
            # font_family='mine',
            size=15,
            ),
        content=ft.Column(
            spacing = 5,
            controls=[
                suport_category,
                suport_texto,
                btn_send_report,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        shape= ft.RoundedRectangleBorder(radius=5),
    )


    #Sección para que salga todo en la pagina de settings
    setting_page = ft.Stack(
        [
            ft.Container(
                content=ft.Column(
                    controls=[
                        title,
                        contenedor,
                        file_picker,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
            ),
        ],
        width=681,
        height=478,
    )

    return setting_page

