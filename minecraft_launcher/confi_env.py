import os
# Variables del Launcher
LAUNCHER_VERSION = '1.0.6'
USER_WINDOWS = os.environ["USERNAME"]
MINECRAFT_DIRECTORY = f"C://Users//{USER_WINDOWS}//AppData//Roaming//.xlauncher"
RUTA_JSON = f"{MINECRAFT_DIRECTORY}//configuration.json"
RUTA_JAVA = f"{MINECRAFT_DIRECTORY}//runtime//jre-legacy//windows-x64//jre-legacy//bin//java.exe"

# Variables para los reportes bug etc
TOKEN = '5998213610:AAE44x-5TRooCXmB-74SIe9NAJvKe5wjqqc' #Pones el token del bot de telegram. https://t.me/BotFather
GRUPO_ID = -1001677501664
MESSAGE_THREAD_ID = 1285 # En caso de que tengas un grupo con temas pon el id del tema al que quieres enviar los reportes de los usuarios en caso de que no tengas un super-grupo dejar en None para que se envié al chat general.