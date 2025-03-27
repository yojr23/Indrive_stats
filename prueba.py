import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter 

def grafico_barras_dias_trabajo(data):
    """
    Genera un gráfico de barras para la pregunta: ¿En qué días de la semana sueles trabajar con mayor frecuencia?
    """
        # Crear una lista para almacenar todos los días extraídos
    dias_totales = []

    # Separar las respuestas múltiples y añadir a la lista
    for respuesta in data['¿En qué días de la semana sueles trabajar con mayor frecuencia?']:
        if pd.notna(respuesta):
            dias_totales.extend([dia.strip() for dia in respuesta.split(',')])

    # Mostrar todos los días detectados para verificación
    #print("Días detectados:", dias_totales)

    # Contar la frecuencia de cada día usando Counter
    contador=Counter(dias_totales)
    print(contador)
    
    
    conteo_dias = dict(contador)  # Convertimos explícitamente a diccionario
    # Ordenar y completar días faltantes
    dias_ordenados = {dia: conteo_dias.get(dia, 0) for dia in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']}
    #print(dias_ordenados)

    
    
    # Graficar
    plt.figure(figsize=(10, 6))
    ax = dias_contados.plot(kind='bar', color='purple')
    plt.title('¿En qué días de la semana sueles trabajar con mayor frecuencia?')
    plt.xlabel('Días de la Semana')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.legend(['Frecuencia'], loc="upper right")

    # Añadir valores encima de las barras
    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2, p.get_height()), 
                    ha='center', va='bottom')

    plt.savefig('grafico_barras_dias_trabajo_test.png', bbox_inches='tight')
    plt.show()


