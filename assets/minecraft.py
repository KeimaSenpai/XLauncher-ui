import os
import json
import subprocess
import minecraft_launcher_lib

user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"
ruta_json = f"{minecraft_directory}//configuracion.json"

async def play_mine():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(ruta_json, 'r') as file:
        data = json.load(file)

    if 'Nombre' in data and 'RAM' in data:
        mine_user = data['Nombre']
        ram = data['RAM']
        java_ruta = data.get('Java', None)

    print('▨ Versiones Instaladas ▨')
    forts = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
    for fort in forts:
        print(fort['id'])
    print('\n▐Digame la versión')
    version = input('» ')

    options = {
        'username': mine_user,
        'uuid': '',
        'token': '',
        'executablePath':f'{java_ruta}',
        'defaultExecutablePath':f'{java_ruta}',

        "jvmArguments": [
            f"-Xmx{ram}G",
            f"-Xms{ram}G",
            "-Xmn668m",
            "-XX:+DisableExplicitGC",
            "-XX:+UseConcMarkSweepGC",
            "-XX:+UseParNewGC",
            "-XX:+UseNUMA",
            "-XX:+CMSParallelRemarkEnabled",
            "-XX:MaxTenuringThreshold=15",
            "-XX:MaxGCPauseMillis=30",
            "-XX:GCPauseIntervalMillis=150",
            "-XX:+UseAdaptiveGCBoundary",
            "-XX:-UseGCOverheadLimit",
            "-XX:+UseBiasedLocking",
            "-XX:SurvivorRatio=8",
            "-XX:TargetSurvivorRatio=90",
            "-XX:MaxTenuringThreshold=15",
            "-Dfml.ignorePatchDiscrepancies=true",
            "-Dfml.ignoreInvalidMinecraftCertificates=true",
            "-XX:+UseFastAccessorMethods",
            "-XX:+UseCompressedOops",
            "-XX:+OptimizeStringConcat",
            "-XX:+AggressiveOpts",
            "-XX:ReservedCodeCacheSize=2048m",
            "-XX:+UseCodeCacheFlushing",
            "-XX:SoftRefLRUPolicyMSPerMB=10000",
            "-XX:ParallelGCThreads=10"
            ],  # The jvmArguments
        "launcherVersion": "1.0.2",
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        version, minecraft_directory, options)
    subprocess.run(minecraft_command)
    await play_mine()