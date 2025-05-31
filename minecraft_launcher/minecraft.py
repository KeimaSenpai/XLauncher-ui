import json
import os
import subprocess
import threading
import minecraft_launcher_lib as mll
import platform

import requests

from minecraft_launcher.confi_env import MINECRAFT_DIRECTORY, RUTA_JAVA, RUTA_JSON, GRUPO_ID, MESSAGE_THREAD_ID, TOKEN, LAUNCHER_VERSION

def latest_versions():
    versiones = []
    version = mll.utils.get_installed_versions(MINECRAFT_DIRECTORY)
    for ver in version:
        if ver["type"] == "release":
            versiones.append(ver["id"])
    return versiones

async def list_versions():
    versioneslis = []
    versionlis = mll.utils.get_version_list()
    for ver in versionlis:
        if ver["type"] == "release" or ver["type"] == "snapshot":
            versioneslis.append(ver["id"])
    return versioneslis


def save_config(mine_user=None, uuid=None, version=None, ram=None, java=None):
    # Verificar si el archivo existe
    if not os.path.exists(RUTA_JSON):
        # Si no existe, crear el diccionario con los valores proporcionados
        data = {
            "username": mine_user if mine_user is not None else "",
            "uuid": uuid if uuid is not None else "",
            "token": "",
            "ram": ram if ram is not None else "",
            "version": version if version is not None else "",
            "java": java if java is not None else "",
        }
    else:
        # Si el archivo existe, cargar los datos existentes
        with open(RUTA_JSON, "r") as f:
            data = json.load(f)

    # Actualizar los valores solo si se pasan en la función
    if mine_user is not None:
        data["username"] = mine_user
    if uuid is not None:
        data["uuid"] = uuid
    if version is not None:
        data["version"] = version
    if ram is not None:
        data["ram"] = ram
    if java is not None:
        data["java"] = java

    # Guardar los datos actualizados en el archivo
    with open(RUTA_JSON, "w") as f:
        json.dump(data, f, indent=4)

# def launch_minecraft(e):
#     # Crear y comenzar un hilo separado para ejecutar play_mine
#     threading.Thread(target=play_mine).start()


async def play_mine(e):
    global options
    if os.path.exists(RUTA_JSON):
        with open(RUTA_JSON, "r") as file:
            data = json.load(file)

        if "username" in data and "ram" in data:
            mine_user = data["username"]
            version = data["version"]
            ram = data["ram"]
            java= data["java"]

        
        options = {
            "username": mine_user,
            "uuid": '',
            "token": "",
            "executablePath": java, 
            "defaultExecutablePath": RUTA_JAVA,
            "jvmArguments": [
                f"-Xmx{ram}G",
                f"-Xms{ram}G",
            ],  # The jvmArguments
            "launcherVersion": f"{LAUNCHER_VERSION}",
        }

        # Ejecutar Minecraft
        minecraft_command = mll.command.get_minecraft_command(
            version, MINECRAFT_DIRECTORY, options
        )
        subprocess.run(minecraft_command, 
                       creationflags=subprocess.CREATE_NO_WINDOW

                    )
    else:
        print('error')
        pass


def enviar_report(tipo, reporte):
    # Obtener el nombre del sistema operativo y versión
    nombre_sistema = platform.system()
    version_sistema = platform.version()

    text = f"""
<b>Reporte de XLauncher</b>
<b>Tipo:</b> <i>#{tipo}</i>
<b>SO:</b> <i>{nombre_sistema} v{version_sistema}</i>

<blockquote expandable>{reporte}</blockquote>
"""
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        "chat_id": GRUPO_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    # Verificar si la variable MESSAGE_THREAD_ID está definida y no es None
    if 'MESSAGE_THREAD_ID' in globals() and MESSAGE_THREAD_ID is not None:
        payload["message_thread_id"] = MESSAGE_THREAD_ID

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Mensaje enviado.")
    else:
        print("Error", response.status_code)