import pandas as pd

# Cargar datos
data = pd.read_csv('data/bd_estad.csv')

print("Medidas descriptivas para horas trabajadas")

print("¿Cuántas horas trabajas en un día típico?")

horas = data['¿Cuántas horas trabajas en un día típico?'].dropna().astype(float)
print("Media:", horas.mean())
print("Mediana:", horas.median())
print("Moda:", horas.mode()[0])
print("Varianza:", horas.var())
print("Desviación estándar:", horas.std())

intervalos = data['¿En qué intervalo de tiempo sueles comenzar tu jornada laboral?'].value_counts(normalize=True)
print("Probabilidades de trabajar en cada intervalo:")
print(intervalos)

import pandas as pd
from collections import Counter
import unicodedata

def eliminar_acentos(texto):
    """
    Elimina acentos de una cadena de texto.
    """
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in texto_normalizado if not unicodedata.combining(c))

# Leer el archivo
data = pd.read_csv('data/bd_estad.csv')

# Separar respuestas múltiples y normalizar
dias = data['¿En qué días de la semana sueles trabajar con mayor frecuencia?'].str.split(',')
dias_exploded = dias.explode().str.strip().apply(eliminar_acentos)

print("¿En qué días de la semana sueles trabajar con mayor frecuencia?")
# Contar frecuencias
frecuencia_dias = Counter(dias_exploded)
print("Frecuencia de días normalizados:", frecuencia_dias)
