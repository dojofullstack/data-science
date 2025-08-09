import requests
import zipfile
import os

ulr_dataframe = "https://www.kaggle.com/api/v1/datasets/download/arnabchaki/data-science-salaries-2023"


def download_dataframe(url_dataframe):
    response = requests.get(url_dataframe)
    # print(response.content)

    print(response.status_code)
    with open("data/data-science-salaries-2023.zip", "wb") as file:
        file.write(response.content)

    # Extraer el fichero ZIP
    extract_zip("data/data-science-salaries-2023.zip", "data/")
    print("Archivo descargado y extraído correctamente.")


def extract_zip(zip_path, extract_to):
    """
    Extrae un archivo ZIP y guarda los archivos en el directorio especificado
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Listar archivos en el ZIP
            print(f"Archivos en el ZIP: {zip_ref.namelist()}")
            
            # Extraer todos los archivos
            zip_ref.extractall(extract_to)
            print(f"Archivos extraídos en: {extract_to}")
            
            # Opcional: eliminar el archivo ZIP después de extraer
            os.remove(zip_path)
            print(f"Archivo ZIP {zip_path} eliminado.")
            
    except zipfile.BadZipFile:
        print("Error: El archivo no es un ZIP válido.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo ZIP.")


#download_dataframe(ulr_dataframe)