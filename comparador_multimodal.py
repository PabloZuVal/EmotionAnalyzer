import json
import csv
from clasificador_texto import analizar_emocion, diccionario_emociones
from clasificador_imagen import predecir_emocion_desde_imagen, cargar_modelo
import os

def cargar_frases(archivo_json):
    """
    Carga las frases desde el archivo JSON
    """
    with open(archivo_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        # Verificar que los datos son una lista de diccionarios con la estructura esperada
        if not isinstance(datos, list):
            raise ValueError("El archivo JSON debe contener una lista de frases")
        return datos

def comparar_emociones(emocion_texto, emocion_imagen):
    """
    Compara si las emociones detectadas en texto e imagen coinciden
    """
    return emocion_texto == emocion_imagen

def procesar_multimodal(datos_frases, directorio_imagenes, model):
    """
    Procesa tanto el texto como las imágenes y compara los resultados
    """
    resultados = []
    
    for dato in datos_frases:
        # Extraer la frase del diccionario
        frase = dato['frase']
        path_imagen = dato['imagen']  # Ya incluye la ruta completa
        
        # Analizar texto
        emocion_texto, puntuaciones_texto = analizar_emocion(frase, diccionario_emociones)
        
        # Analizar imagen si existe
        if os.path.exists(path_imagen):
            emocion_imagen, puntuaciones_imagen = predecir_emocion_desde_imagen(path_imagen, model)
        else:
            print(f"Advertencia: No se encontró la imagen {path_imagen}")
            emocion_imagen = "no_encontrada"
            puntuaciones_imagen = {}
        
        # Determinar si coinciden
        coincide = comparar_emociones(emocion_texto, emocion_imagen)
        
        # Guardar resultados
        resultados.append({
            'frase': frase,
            'imagen': path_imagen,
            'emocion_texto': emocion_texto,
            'emocion_imagen': emocion_imagen,
            'coincide': coincide,
            'emocion_esperada': dato.get('emocion', 'no_especificada'),
            'puntuaciones_texto': puntuaciones_texto,
            'puntuaciones_imagen': puntuaciones_imagen
        })
    
    return resultados

def guardar_resultados_csv(resultados, archivo_salida='resultados.csv'):
    """
    Guarda los resultados en un archivo CSV
    """
    with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Escribir encabezado
        writer.writerow(['frase', 'imagen', 'emocion_texto', 'emocion_imagen', 'emocion_esperada', 'coincide'])
        
        # Escribir datos
        for r in resultados:
            writer.writerow([
                r['frase'],
                r['imagen'],
                r['emocion_texto'],
                r['emocion_imagen'],
                r['emocion_esperada'],
                'Sí' if r['coincide'] else 'No'
            ])

def analizar_divergencias(resultados):
    """
    Analiza las causas de divergencia entre modalidades
    """
    total = len(resultados)
    coincidencias = sum(1 for r in resultados if r['coincide'])
    divergencias = total - coincidencias
    
    print("\nAnálisis de Divergencias:")
    print(f"Total de casos analizados: {total}")
    print(f"Casos coincidentes: {coincidencias} ({(coincidencias/total)*100:.1f}%)")
    print(f"Casos divergentes: {divergencias} ({(divergencias/total)*100:.1f}%)")
    
    # Analizar patrones de divergencia
    if divergencias > 0:
        print("\nPatrones de divergencia más comunes:")
        divergencias_dict = {}
        for r in resultados:
            if not r['coincide']:
                par = (r['emocion_texto'], r['emocion_imagen'])
                divergencias_dict[par] = divergencias_dict.get(par, 0) + 1
        
        # Mostrar los patrones más comunes
        for (emocion_texto, emocion_imagen), count in sorted(divergencias_dict.items(), 
                                                           key=lambda x: x[1], 
                                                           reverse=True)[:3]:
            print(f"Texto: {emocion_texto} → Imagen: {emocion_imagen}: {count} casos")

if __name__ == "__main__":
    # Cargar el modelo
    model = cargar_modelo("fer2013_mini_XCEPTION.99-0.65.hdf5")
    
    # Cargar frases
    frases = cargar_frases('frases.json')
    
    # Procesar datos
    resultados = procesar_multimodal(frases, 'imagenes', model)
    
    # Guardar resultados
    guardar_resultados_csv(resultados)
    
    # Analizar divergencias
    analizar_divergencias(resultados)
    
    print("\nProceso completado. Los resultados se han guardado en 'resultados.csv'")
