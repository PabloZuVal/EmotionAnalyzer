# Reconocimiento Multimodal de Emociones

Este proyecto implementa un sistema para reconocer emociones a partir de texto e imágenes faciales, y comparar si ambas modalidades expresan la misma emoción. La actividad está diseñada para desarrollar competencias en procesamiento de texto, análisis de imágenes y la integración de señales multimodales.

---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Objetivos](#objetivos)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura de Archivos](#estructura-de-archivos)
- [Datos](#datos)
- [Modelo Preentrenado](#modelo-preentrenado)
- [Resultados](#resultados)
- [Créditos](#créditos)
- [Notas Adicionales](#notas-adicionales)

---

## Descripción

El sistema analiza emociones en dos modalidades:
- **Texto:** Utilizando un diccionario emocional para identificar la emoción dominante en frases.
- **Imágenes:** Empleando un modelo preentrenado (FER2013) para clasificar emociones en imágenes faciales.
- **Comparación:** Determina si las emociones detectadas en el texto y la imagen coinciden.

---

## Objetivos

El objetivo de esta actividad es diseñar e implementar un sistema capaz de:
- Detectar emociones expresadas en una frase escrita.
- Detectar emociones expresadas en una imagen facial.
- Comparar si ambas modalidades expresan la misma emoción.
- Reflexionar sobre las posibles causas de divergencia entre las modalidades.

---

## Tecnologías

- **Python 3.8+**
- **TensorFlow**: Para el modelo de reconocimiento de emociones en imágenes.
- **NumPy**: Para operaciones numéricas.
- **Pillow**: Para el manejo de imágenes.
- **Opcional**:
  - **OpenCV**: Para visualización y depuración de imágenes.
  - **Matplotlib**: Para visualización de resultados.
  - **spaCy**: Para lematización en el análisis de texto.

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/PabloZuVal/EmotionAnalyzer.git
   cd EmotionAnalyzer
   ```

2. Instala las dependencias listadas en `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. (Opcional) Si deseas usar lematización en el análisis de texto, instala spaCy y el modelo en español:
   ```bash
   pip install spacy
   python -m spacy download es_core_news_sm
   ```

---

## Uso

El proyecto consta de tres componentes principales:

1. **Análisis de Texto** (`clasificador_texto.py`):
   - Analiza emociones en frases usando el diccionario proporcionado.
   - Ejecución:
     ```bash
     python clasificador_texto.py
     ```

2. **Análisis de Imágenes** (`clasificador_imagen.py`):
   - Analiza emociones en imágenes faciales usando el modelo preentrenado.
   - Ejecución:
     ```bash
     python clasificador_imagen.py
     ```

3. **Comparación Multimodal** (`comparador_multimodal.py`):
   - Compara las emociones detectadas en texto e imágenes y genera un archivo de resultados.
   - Ejecución:
     ```bash
     python comparador_multimodal.py
     ```

---

## Estructura de Archivos

```bash
.
├── clasificador_imagen.py        # Script para análisis de emociones en imágenes
├── clasificador_texto.py         # Script para análisis de emociones en texto
├── comparador_multimodal.py      # Script para comparación de emociones y generación de resultados
├── diccionario_emociones.py      # Diccionario de emociones para análisis de texto
├── fer2013_mini_XCEPTION.99-0.65.hdf5  # Modelo preentrenado para reconocimiento de emociones en imágenes
├── frases.json                   # Archivo JSON con frases y emociones asociadas
├── imagenes/                     # Directorio con imágenes faciales
│   ├── 01.png
│   ├── 02.png
│   ├── ...
├── requirements.txt              # Lista de dependencias
└── README.md                     # Este archivo
```

---

## Datos

- **`frases.json`**: Contiene frases en español asociadas a emociones básicas (alegría, tristeza, enojo, etc.).
- **`imagenes/`**: Directorio con imágenes faciales que muestran emociones visibles.

---

## Modelo Preentrenado

El modelo **`fer2013_mini_XCEPTION.99-0.65.hdf5`** es un modelo preentrenado para clasificar emociones en imágenes faciales, basado en el dataset FER2013. El modelo espera imágenes de **64x64 píxeles en escala de grises**. Las emociones que puede detectar son: enojo, asco, miedo, alegría, tristeza, sorpresa y neutral.

---

## Resultados

El script `comparador_multimodal.py` genera un archivo **`resultados.csv`** con las siguientes columnas:
- `frase`: La frase analizada.
- `imagen`: El nombre del archivo de la imagen asociada.
- `emocion_texto`: Emoción detectada en el texto.
- `emocion_imagen`: Emoción detectada en la imagen.
- `coincide`: Indica si las emociones coinciden ("sí" o "no").

Además, se debe entregar un **`informe_reflexion.pdf`** con un análisis de los resultados y posibles causas de divergencia entre las modalidades.

---

## Créditos

- **Modelo FER2013**: [Fuente del modelo, si aplica]
- **Diccionario de Emociones**: [Fuente, si aplica]

---

## Notas Adicionales

- Asegúrate de que las imágenes estén en el formato correcto (**64x64 píxeles, escala de grises**) para el modelo de imágenes.
- El análisis de texto considera negaciones (como "no", "nunca") para ajustar los puntajes emocionales.
- Para mejorar el análisis de texto, puedes usar lematización instalando spaCy y el modelo `es_core_news_sm`.

---

**¡Gracias por usar este proyecto!** Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactar al equipo.