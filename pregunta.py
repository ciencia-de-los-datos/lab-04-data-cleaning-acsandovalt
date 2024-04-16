"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    # Cargar el archivo CSV en un DataFrame
    archivo_csv = 'solicitudes_credito.csv'
    df = pd.read_csv(archivo_csv, sep=';')

    df.drop(df.columns[0], axis=1, inplace=True)

    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ').str.replace('-', ' ')
    df['idea_negocio'] = df['idea_negocio'].str.replace(r'( en $| en$| de $| de$| el $| el$| y $| y$)', '', regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.replace(r'( para $| para$)', '', regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.rstrip()
    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].str.replace('_', ' ').str.replace('-', ' ').str.replace('nari¿o', 'nariño').str.replace('bel¿n', 'belen').str.replace('veinte', '20')
    df['barrio'] = df['barrio'].str.replace(r'( no.$| no. $| no. 1$| no.1$| no. 2$| no.2$| parte alta|cabecera| alto)', '', regex=True)
    df['barrio'] = df['barrio'].str.rstrip().str.lstrip()
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce')
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d/%m/%Y')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(r'[^\d.]', '', regex=True).astype(float)
    df['línea_credito'] = df['línea_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ').str.replace('-', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('soli diaria', 'solidaria')
    df['línea_credito'] = df['línea_credito'].str.replace(r'(. $)', '', regex=True)
    df['línea_credito'] = df['línea_credito'].str.rstrip().str.lstrip()
                
    df.drop_duplicates(inplace=True)
    
    # Contar
    sexo = df['sexo'].value_counts()
    tipo_de_emprendimiento = df['tipo_de_emprendimiento'].value_counts()
    idea_negocio = df['idea_negocio'].value_counts()
    barrio = df['barrio'].value_counts()
    estrato = df['estrato'].value_counts()
    comuna_ciudadano = df['comuna_ciudadano'].value_counts()
    fecha_de_beneficio = df['fecha_de_beneficio'].value_counts()
    monto_del_credito = df['monto_del_credito'].value_counts()
    línea_credito = df['línea_credito'].value_counts()
    
    print(sexo)
    #print(tipo_de_emprendimiento.sort_index())
    #print(idea_negocio.sort_index())
    #print(barrio)
    #print(estrato.sort_index())
    #print(comuna_ciudadano.sort_index())
    #print(fecha_de_beneficio.sort_index())
    #print(monto_del_credito.sort_index())
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        #print(línea_credito.sort_index())
        
clean_data()
