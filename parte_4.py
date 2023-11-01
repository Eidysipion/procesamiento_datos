import requests

def descargar_datos_como_csv(url, nombre_archivo):
    try:
        
        response = requests.get(url)
        
    
        if response.status_code == 200:
            
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(response.content)
            print(f"Los datos se han descargado y guardado en '{nombre_archivo}'.")
        else:
            print(f"Error al descargar los datos. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")


url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre_archivo = "fallo_cardiaco.csv"
descargar_datos_como_csv(url, nombre_archivo)
