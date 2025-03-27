import matplotlib.pyplot as plt
import pandas as pd
import os
import unicodedata
from collections import Counter 

# Crear carpeta para guardar las gráficas si no existe
os.makedirs("graficas", exist_ok=True)

def grafico_histograma_horas_trabajadas(data):
    """
    Genera un histograma para la pregunta: ¿Cuántas horas trabajas en un día típico?
    """
    horas = pd.to_numeric(data['¿Cuántas horas trabajas en un día típico?'], errors='coerce').dropna()
    plt.figure(figsize=(8, 6))
    plt.hist(horas, bins=range(int(horas.min()), int(horas.max()) + 2), color='skyblue', edgecolor='black', align='left')
    plt.title('Distribución de las horas trabajadas por día')
    plt.xlabel('Horas trabajadas')
    plt.ylabel('Frecuencia')
    plt.xticks(range(int(horas.min()), int(horas.max()) + 1))
    plt.legend(['Horas trabajadas'], loc="upper right")
    plt.savefig('graficas/grafico_histograma_horas_trabajadas.png', bbox_inches='tight')
    plt.show()


def grafico_pastel_intervalo_tiempo(data):
    valores = data['¿En qué intervalo de tiempo sueles comenzar tu jornada laboral?'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels=valores.index, autopct='%1.1f%%', startangle=90)
    plt.title('¿En qué intervalo de tiempo sueles comenzar tu jornada laboral?')
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig('graficas/grafico_pastel_intervalo_tiempo.png', bbox_inches='tight')
    plt.show()

def eliminar_acentos(texto):
    """
    Convierte un texto eliminando los acentos.
    
    Parámetros:
    texto (str): Cadena de texto con posibles acentos.

    Retorna:
    str: Cadena de texto sin acentos.
    """
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sin_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))
    return texto_sin_acentos

def grafico_barras_dias_trabajo(data):
    """
    Genera un gráfico de barras para la pregunta: ¿En qué días de la semana sueles trabajar con mayor frecuencia?
    """
    # Crear una lista para almacenar todos los días extraídos
    dias_totales = []

    # Separar las respuestas múltiples y añadir a la lista
    for respuesta in data['¿En qué días de la semana sueles trabajar con mayor frecuencia?']:
        if pd.notna(respuesta):
            dias_totales.extend([eliminar_acentos(dia.strip()) for dia in respuesta.split(',')])

    # Mostrar todos los días detectados para verificación
    print("Días detectados (normalizados):", dias_totales)

    # Contar la frecuencia de cada día usando Counter
    contador = Counter(dias_totales)
    print("Conteo de días:", contador)
    
    # Ordenar y completar días faltantes
    dias_ordenados = {dia: contador.get(dia, 0) for dia in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']}

    # Graficar
    plt.figure(figsize=(10, 6))
    ax = pd.Series(dias_ordenados).plot(kind='bar', color='purple')
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
    
def grafico_pastel_mayores_ganancias(data):
    ganancias = data['¿Experimentas mayores ganancias en algún horario específico?'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(ganancias, labels=ganancias.index, autopct='%1.1f%%', startangle=90)
    plt.title('¿Experimentas mayores ganancias en algún horario específico?')
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.savefig('graficas/grafico_pastel_mayores_ganancias.png', bbox_inches='tight')
    plt.show()

def grafico_barras_carreras(data):
    carreras = data['¿Cuántas carreras realizas en promedio durante un turno completo?'].value_counts()
    plt.figure(figsize=(10, 6))
    carreras.plot(kind='bar', color='blue')
    plt.title('¿Cuántas carreras realizas en promedio durante un turno completo?')
    plt.xlabel('Número de Carreras')
    plt.ylabel('Frecuencia')
    plt.legend(['Frecuencia'], loc="upper right")
    plt.savefig('graficas/grafico_barras_carreras.png', bbox_inches='tight')
    plt.show()

def grafico_barras_ingresos_varian(data):
    variacion = data['¿Consideras que tus ingresos por kilómetro varían significativamente entre diferentes horarios?'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    variacion.plot(kind='bar', color='orange')
    plt.title('¿Consideras que tus ingresos por kilómetro varían significativamente entre diferentes horarios?')
    plt.xlabel('Nivel de acuerdo (1 a 5)')
    plt.ylabel('Frecuencia')
    plt.legend(['Frecuencia'], loc="upper right")
    plt.savefig('graficas/grafico_barras_ingresos_varian.png', bbox_inches='tight')
    plt.show()

def grafico_linea_kilometros(data):
    """
    Genera un gráfico de líneas para la pregunta: ¿Cuántos kilómetros recorres en un día promedio?
    """
    kilometros = pd.to_numeric(data['¿Cuántos kilómetros recorres en un día promedio?'], errors='coerce').dropna()
    frecuencia = kilometros.value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    plt.plot(frecuencia.index, frecuencia.values, marker='o', linestyle='-', color='green')
    plt.title('Tendencia de kilómetros recorridos por día')
    plt.xlabel('Kilómetros')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.legend(['Frecuencia'], loc="upper right")
    plt.savefig('graficas/grafico_linea_kilometros.png', bbox_inches='tight')
    plt.show()

def grafico_linea_ganancia_kilometro(data):
    """
    Genera un gráfico de líneas para la pregunta: ¿Cuál es tu ganancia promedio por kilómetro en un día normal?
    """
    ganancia = pd.to_numeric(data['¿Cuál es tu ganancia promedio por kilómetro en un día normal?'], errors='coerce').dropna()
    frecuencia = ganancia.value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    plt.plot(frecuencia.index, frecuencia.values, marker='o', linestyle='-', color='red')
    plt.title('Tendencia de ganancia promedio por kilómetro')
    plt.xlabel('Ganancia promedio ($)')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.legend(['Frecuencia'], loc="upper right")
    plt.savefig('graficas/grafico_linea_ganancia_kilometro.png', bbox_inches='tight')
    plt.show()
def generar_graficas(data):
    """
    Genera todas las gráficas en función de las preguntas del formulario.
    """
    grafico_histograma_horas_trabajadas(data)
    grafico_pastel_intervalo_tiempo(data)
    grafico_barras_dias_trabajo(data)
    grafico_pastel_mayores_ganancias(data)
    grafico_barras_carreras(data)
    grafico_barras_ingresos_varian(data)
    grafico_linea_kilometros(data)
    grafico_linea_ganancia_kilometro(data)