import os
import random

def generar_archivo_corrupto(nombre_archivo, extension, tamano_kb=100):
    """Crea un archivo completamente inutilizable con datos aleatorios."""
    nombre_completo = f"{nombre_archivo}.{extension}"
    try:
        with open(nombre_completo, 'wb') as archivo:
            archivo.write(os.urandom(tamano_kb * 1024))  # Genera bytes aleatorios
        print(f"Archivo corrupto creado: {nombre_completo} ({tamano_kb} KB)")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

def corromper_archivo_existente(ruta_entrada, ruta_salida, bytes_a_corromper=10):
    """Corrompe un archivo existente modificando bytes aleatorios."""
    try:
        with open(ruta_entrada, 'rb') as archivo_original:
            datos = bytearray(archivo_original.read())
        
        print(f"El archivo original tiene {len(datos)} bytes.")
        for _ in range(bytes_a_corromper):
            indice = random.randint(0, len(datos) - 1)
            datos[indice] = random.randint(0, 255)  # Sobrescribe con un byte aleatorio
        
        with open(ruta_salida, 'wb') as archivo_corrupto:
            archivo_corrupto.write(datos)
        
        print(f"Archivo corrupto creado: {ruta_salida}")
    except Exception as e:
        print(f"Error al corromper el archivo: {e}")

def main():
    print("=== Herramienta para Crear Archivos Corruptos ===")
    print("1. Generar archivo corrupto desde cero")
    print("2. Corromper archivo existente")
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        nombre_archivo = input("Nombre del archivo a crear (sin extensión): ").strip()
        extension = input("Ingresa la extensión del archivo (ejemplo: docx, xlsx, txt): ").strip()
        tamano_kb = int(input("Tamaño del archivo en KB (por defecto 100): ") or 100)
        generar_archivo_corrupto(nombre_archivo, extension, tamano_kb)
    elif opcion == "2":
        ruta_entrada = input("Ruta del archivo original: ").strip()
        ruta_salida = input("Ruta para guardar el archivo corrupto: ").strip()
        bytes_a_corromper = int(input("Número de bytes a corromper (por defecto 10): ") or 10)
        corromper_archivo_existente(ruta_entrada, ruta_salida, bytes_a_corromper)
    else:
        print("Opción no válida. Saliendo.")

if __name__ == "__main__":
    main()
