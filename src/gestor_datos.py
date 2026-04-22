import json
import os
import sys


# esta funcion permite encontrar los recursos del juego
def ruta_recurso(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class GestorDatos:
    @staticmethod
    def cargar_palabras(nombre_archivo):

        # 1. Apuntamos a tu carpeta 'data' tal como se ve en tu imagen
        ruta_relativa = os.path.join("data", f"{nombre_archivo}.json")

        # 2. La convertimos a la ruta absoluta segura para el .exe
        ruta_segura = ruta_recurso(ruta_relativa)

        try:
            with open(ruta_segura, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos.get("palabras", [])

        except FileNotFoundError:
            print(f"⚠️ Error: No se encontró el archivo en {ruta_segura}")
            return []

        except json.JSONDecodeError:
            print(
                f"⚠️ Error: El archivo {nombre_archivo}.json tiene un formato inválido"
            )
            return []
