import pandas as pd

data = pd.read_csv('fallo_cardiaco.csv')

def procesar_datos(data):
    
    if data.isnull().sum().sum() == 0:
        print("No hay valores faltantes.")
    else:
        print("Existen valores faltantes en el conjunto de datos.")

    
    if data.duplicated().sum() == 0:
        print("No hay filas repetidas.")
    else:
        print("Existen filas repetidas en el conjunto de datos.")


    data['Age_Category'] = pd.cut(data['age'], bins=[0, 12, 19, 39, 59, float('inf')],
                                  labels=['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor'])

   
    data.to_csv('datos_procesados.csv', index=False)

    return data


data_procesada = procesar_datos(data)
