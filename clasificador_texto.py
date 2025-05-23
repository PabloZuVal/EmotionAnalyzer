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
    # Mejorado para capturar más palabras y signos de puntuación
    tokens = re.findall(r'\b\w+\b|[!¡?¿]', frase)
    return tokens

def analizar_emocion(frase, diccionario):
    """
    Analiza la emoción predominante en una frase usando el diccionario de emociones
    """
    tokens = preprocesar(frase)
    puntuaciones = defaultdict(float)  # Cambiado a float para manejar pesos
    negacion = False
    intensificadores = {'muy': 1.5, 'mucho': 1.5, 'demasiado': 2.0, 'super': 2.0, 'tan': 1.5}
    
    for i, token in enumerate(tokens):
        # Detectar negaciones
        if token in ["no", "nunca", "jamás", "ni"]:
            negacion = True
            continue
            
        # Detectar intensificadores
        if token in intensificadores:
            continue
        
        # Aplicar intensificadores al siguiente token emocional
        intensificador = 1.0
        if i > 0 and tokens[i-1] in intensificadores:
            intensificador = intensificadores[tokens[i-1]]
            
        if token in diccionario:
            for emocion, puntaje in diccionario[token].items():
                if negacion:
                    # Invertimos el puntaje y la emoción en caso de negación
                    emocion_opuesta = obtener_emocion_opuesta(emocion)
                    puntuaciones[emocion_opuesta] += abs(puntaje) * intensificador
                else:
                    puntuaciones[emocion] += puntaje * intensificador
            
        # Reset negación después de procesar la siguiente palabra emocional
        if negacion and token in diccionario:
            negacion = False
    
    # Ajustar puntuaciones basadas en signos de exclamación
    exclamaciones = sum(1 for t in tokens if t in ['!', '¡'])
    if exclamaciones > 0:
        factor = 1 + (exclamaciones * 0.2)  # Aumenta la intensidad un 20% por cada signo
        for emocion in puntuaciones:
            puntuaciones[emocion] *= factor
    
    if not puntuaciones:
        return "neutral", {}
    
    # Encontrar la emoción con mayor puntaje absoluto
    emocion_predominante = max(puntuaciones.items(), key=lambda x: abs(x[1]))
    return emocion_predominante[0], dict(puntuaciones)

def obtener_emocion_opuesta(emocion):
    """
    Retorna la emoción opuesta para casos de negación
    """
    opuestos = {
        'alegría': 'tristeza',
        'tristeza': 'alegría',
        'enojo': 'neutral',
        'miedo': 'neutral',
        'asco': 'neutral',
        'sorpresa': 'neutral',
        'neutral': 'neutral'
    }
    return opuestos.get(emocion, 'neutral')

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
