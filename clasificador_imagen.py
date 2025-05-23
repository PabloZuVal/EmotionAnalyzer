from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Etiquetas del modelo
emotion_labels_en = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
emotion_labels_es = {
    'angry': 'enojo',
    'disgust': 'asco',
    'fear': 'miedo',
    'happy': 'alegría',
    'sad': 'tristeza',
    'surprise': 'sorpresa',
    'neutral': 'neutral'
}

def cargar_modelo(ruta_modelo):
    """
    Carga el modelo pre-entrenado desde la ruta especificada
    """
    return load_model(ruta_modelo, compile=False)

# Preprocesamiento de imagen
def cargar_imagen_gris_64x64(path):
    img = image.load_img(path, color_mode="grayscale", target_size=(64, 64))
    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    return x

# Predicción individual
def predecir_emocion_desde_imagen(path_imagen, model=None):
    """
    Predice la emoción desde una imagen, retornando la emoción y las puntuaciones
    """
    # Si no se proporciona un modelo, usar el modelo global
    if model is None:
        model = load_model("fer2013_mini_XCEPTION.99-0.65.hdf5", compile=False)
        
    x = cargar_imagen_gris_64x64(path_imagen)
    pred = model.predict(x, verbose=0)
    idx = np.argmax(pred)
    emocion_en = emotion_labels_en[idx]
    
    # Crear diccionario de puntuaciones
    puntuaciones = {}
    for i, label in enumerate(emotion_labels_en):
        puntuaciones[emotion_labels_es[label]] = float(pred[0][i])
    
    return emotion_labels_es[emocion_en], puntuaciones

# Proceso completo para carpeta
if __name__ == "__main__":
    # Cargar el modelo
    model = cargar_modelo("fer2013_mini_XCEPTION.99-0.65.hdf5")
    
    carpeta = "imagenes/"
    if not os.path.exists(carpeta):
        print("❌ La carpeta 'imagenes/' no existe.")
        exit()

    imagenes = [f for f in os.listdir(carpeta) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    if not imagenes:
        print("⚠️ No se encontraron imágenes en la carpeta.")
        exit()

    print("🔍 Emociones detectadas por imagen:\n")
    for nombre_imagen in sorted(imagenes):
        path = os.path.join(carpeta, nombre_imagen)
        try:
            emocion, puntuaciones = predecir_emocion_desde_imagen(path, model)
            print(f"Emoción detectada en imagen {nombre_imagen} → {emocion}")
            print(f"Puntuaciones: {puntuaciones}\n")
        except Exception as e:
            print(f"{nombre_imagen} → Error: {e}")
