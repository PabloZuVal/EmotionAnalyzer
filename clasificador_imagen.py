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

# Cargar modelo
model = load_model("fer2013_mini_XCEPTION.99-0.65.hdf5", compile=False)

# Preprocesamiento de imagen
def cargar_imagen_gris_64x64(path):
    img = image.load_img(path, color_mode="grayscale", target_size=(64, 64))
    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    return x

# Predicción individual
def predecir_emocion_desde_imagen(path_imagen):
    x = cargar_imagen_gris_64x64(path_imagen)
    pred = model.predict(x)
    idx = np.argmax(pred)
    emocion_en = emotion_labels_en[idx]
    return emotion_labels_es[emocion_en]

# Proceso completo para carpeta
if __name__ == "__main__":
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
            emocion = predecir_emocion_desde_imagen(path)
            print(f"Emoción detectada en imagen {nombre_imagen} → {emocion}")
        except Exception as e:
            print(f"{nombre_imagen} → Error: {e}")
