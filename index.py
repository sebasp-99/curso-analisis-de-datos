import pandas as pd

datos = 'https://github.com/Twoeme/Prueba2/blob/main/Protein_Supply_Quantity_Data.csv'

#Leer bd
df = pd.read_csv(datos)

df.info()