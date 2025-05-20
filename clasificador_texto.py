import re
from collections import defaultdict
from diccionario_emociones import diccionario_emociones
import json

def preprocesar(frase):
    """
    Preprocesa una frase normalizándola y dividiéndola en tokens
    """
    # Convertir a minúsculas y normalizar acentos
    frase = frase.lower()
    tokens = re.findall(r'\b\w{3,}\b', frase)  # Solo palabras de al menos 3 letras
    return tokens

def analizar_emocion(frase, diccionario):
    """
    Analiza la emoción predominante en una frase usando el diccionario de emociones
    """
    tokens = preprocesar(frase)
    puntuaciones = defaultdict(float)  # Cambiado a float para manejar mejor los decimales
    negacion = False
    
    for i, token in enumerate(tokens):
        if token in ["no", "nunca", "jamás"]:
            negacion = True
            continue
            
        if token in diccionario:
            for emocion, puntaje in diccionario[token].items():
                if negacion:
                    # Invertimos el puntaje en caso de negación
                    puntuaciones[emocion] -= puntaje
                else:
                    puntuaciones[emocion] += puntaje
            
        # Reset negación después de procesar la siguiente palabra
        if negacion and token not in ["no", "nunca", "jamás"]:
            negacion = False
    
    if not puntuaciones:
        return "neutral", {}
    
    # Encontrar la emoción con mayor puntaje absoluto
    emocion_predominante = max(puntuaciones.items(), key=lambda x: abs(x[1]))
    return emocion_predominante[0], dict(puntuaciones)

def procesar_frases(archivo_json):
    """
    Procesa todas las frases del archivo JSON y retorna los resultados
    Compara la emoción detectada con la emoción esperada
    """
    with open(archivo_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    resultados = []
    aciertos = 0
    total = len(datos)
    
    for dato in datos:
        frase = dato['frase']
        emocion_esperada = dato['emocion']
        imagen = dato['imagen']
        
        emocion_detectada, puntuaciones = analizar_emocion(frase, diccionario_emociones)
        
        coincide = emocion_detectada == emocion_esperada
        if coincide:
            aciertos += 1
            
        resultados.append({
            'frase': frase,
            'emocion_esperada': emocion_esperada,
            'emocion_detectada': emocion_detectada,
            'puntuaciones': puntuaciones,
            'imagen': imagen,
            'coincide': coincide
        })
    
    precision = (aciertos / total) * 100 if total > 0 else 0
    
    return resultados, precision

if __name__ == "__main__":
    # Ejemplo de uso con una frase individual
    frase_ejemplo = "Estoy muy feliz con el resultado"
    emocion, detalle = analizar_emocion(frase_ejemplo, diccionario_emociones)
    print(f"\nPrueba individual:")
    print(f"Frase: {frase_ejemplo}")
    print(f"Emoción detectada: {emocion}")
    print(f"Puntajes: {detalle}")
    
    # Procesar todas las frases del archivo JSON
    print("\nProcesando archivo frases.json...")
    resultados, precision = procesar_frases('frases.json')
    
    print(f"\nPrecisión total: {precision:.2f}%")
    print("\nPrimeros 5 resultados del análisis:")
    for resultado in resultados:
        print(f"\nFrase: {resultado['frase']}")
        print(f"Emoción esperada: {resultado['emocion_esperada']}")
        print(f"Emoción detectada: {resultado['emocion_detectada']}")
        print(f"Coincide: {'✓' if resultado['coincide'] else '✗'}")
        print(f"Puntuaciones: {resultado['puntuaciones']}")
