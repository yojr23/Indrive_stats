from cargar_datos import cargar_y_limpiar_csv
from graficas import generar_graficas

def menu():
    print("==== Menú Principal ====")
    print("1. Cargar datos")
    print("2. Generar gráficas")
    print("3. Salir")
    
    df = None
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre_archivo = input("Ingrese el nombre del archivo CSV (debe estar en la carpeta 'data/'): ")
            try:
                df = cargar_y_limpiar_csv(nombre_archivo)
                print("Datos cargados exitosamente.")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"Error al cargar los datos: {e}")
        elif opcion == "2":
            if df is not None:
                generar_graficas(df)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
