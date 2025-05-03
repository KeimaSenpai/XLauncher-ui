import flet as ft
import minecraft_launcher_lib as mll
import urllib.request
from minecraft_launcher.confi_env import MINECRAFT_DIRECTORY
from minecraft_launcher.minecraft import list_versions, save_config


def check_internet():
    try:
        urllib.request.urlopen('https://google.com', timeout=10)
        return True
    except urllib.request.URLError as err: 
        return False

if check_internet():
    versions = list_versions()
else:
    versions = ["No Internet"]

opciones = [ft.dropdown.Option(version) for version in versions]
title = ft.Text('Instalación', font_family='mine_dun', size=30)
pb = ft.ProgressBar(
    width=600, 
    height=10, 
    value=0, 
    color='#5B0098', 
    bgcolor='#1F1F23', 
    border_radius=0
)
dd = ft.Dropdown(
    width=200,
    # height=50,
    bgcolor="#343434",
    focused_bgcolor="#343434",
    border=ft.InputBorder.NONE,
    options=opciones,
)
de = ft.Dropdown(
    width=200,
    bgcolor="#343434",
    border=ft.InputBorder.NONE,
    options=[
            ft.dropdown.Option("Vanilla"),
            ft.dropdown.Option("Forge"),
            ft.dropdown.Option("Fabric"),
        ],
)

downloadtext = ft.ListView(spacing=5, padding=10, auto_scroll=True)
downloadprogress = ft.ListView(width=50, auto_scroll=True)

def infotext(text):
    downloadtext.controls.clear()
    downloadtext.controls.append(
        ft.Row([ft.Text(text, size=14, color='#ffffff', font_family='mine')], alignment="center")
    )
    downloadtext.update()

def infoprog(text):
    downloadprogress.controls.clear()
    downloadprogress.controls.append(
        ft.Row([ft.Text(text, size=14, color='#ffffff', font_family='mine')], alignment="center")
    )
    downloadprogress.update()

def install(e):
    if dd.value == "No Internet Connection":
        infotext("No hay conexión a Internet. No se puede instalar.")
    else:
        if de.value == 'Vanilla':
            infotext(install_mine(dd.value))
        elif de.value == 'Forge':
            forge_version = dd.value
            forge_ob_version = mll.forge.find_forge_version(forge_version)
            infotext(install_forge(forge_ob_version))

        elif de.value == "Fabric":
            fabric_version = dd.value
            fabric_suport_ver = mll.fabric.is_minecraft_version_supported(fabric_version)
            if fabric_suport_ver == False:
                infotext('No es compatible esa versión')
            else:
                infotext(install_fabric(dd.value))
def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=40,
    fill="●",
    printEnd="",
):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "○" * (length - filledLength)
    pb.value = iteration / total
    pb.update()
    infoprog(f"{prefix} {percent}% {suffix}")

def maximum(max_value, value):
    max_value[0] = value

def install_mine(version):
    max_value = [0]
    callback = {
        "setStatus": lambda text: infotext(text),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value),
    }

    mll.install.install_minecraft_version(
        version, MINECRAFT_DIRECTORY, callback=callback
    )
    info = mll.utils.generate_test_options()
    save_config(uuid=info["uuid"], version=version)
    return f"{version} instalada exitosamente."

# Install Forge
def install_forge(forge_ob_version):
    max_value = [0]
    callback = {
        "setStatus": lambda text: infotext(text),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value),
    }

    # Aquí instalamos la versión de Forge usando la función de la librería
    mll.forge.install_forge_version(forge_ob_version, MINECRAFT_DIRECTORY, callback=callback)
    return f"Forge {forge_ob_version} instalado exitosamente."

def install_fabric(version):
    max_value = [0]
    callback = {
        "setStatus": lambda text: infotext(text),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value),
    }

    # Instalamos la versión de Minecraft con Fabric
    mll.fabric.install_fabric(version, MINECRAFT_DIRECTORY, callback=callback)
    return f"Fabric {version} instalado exitosamente."

button_install = ft.ElevatedButton(
    "INSTALAR",
    style=ft.ButtonStyle(
        color="#ffffff",
        bgcolor="#5B0098",
        overlay_color="#0C0C0C",
        shape=ft.RoundedRectangleBorder(radius=3),
        shadow_color="#000000",
        elevation=5,
    ),
    on_click=lambda _: install(dd.value),
)

install_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[
                    title,
                    dd,
                    de,
                    downloadtext,
                    pb,
                    downloadprogress,
                    button_install,
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