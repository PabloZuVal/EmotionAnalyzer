# Reconocimiento Multimodal de Emociones en Texto e Imagen

Este proyecto implementa un sistema de reconocimiento multimodal de emociones que analiza tanto texto como imágenes faciales, comparando si ambas modalidades expresan la misma emoción. Es parte de la Actividad 2 del curso de Computación Afectiva.

## Estado Actual del Proyecto

- **Clasificador de Texto**: 93.33% de precisión en la detección de emociones básicas
- **Clasificador de Imágenes**: Implementado con áreas de mejora identificadas
- **Sistema Multimodal**: 28.3% de coincidencia en análisis combinado (17/60 casos)

---

## Tabla de Contenidos

- [Estado Actual del Proyecto](#estado-actual-del-proyecto)
- [Descripción de la Actividad](#descripción-de-la-actividad)
- [Competencias Desarrolladas](#competencias-desarrolladas)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Resultados y Métricas](#resultados-y-métricas)
- [Entregables](#entregables)
- [Evaluación](#evaluación)

---

## Descripción de la Actividad

El objetivo principal es diseñar e implementar un sistema que:
1. Detecte emociones expresadas en frases escritas en español
2. Identifique emociones en imágenes faciales
3. Compare y analice si ambas modalidades expresan la misma emoción

El sistema utiliza:
- Un diccionario emocional simbólico para el análisis de texto
- El modelo pre-entrenado FER2013 para clasificación de emociones en imágenes
- Un comparador multimodal para analizar coincidencias

---

## Competencias Desarrolladas

- Procesamiento simbólico de emociones desde texto
- Uso de modelos computacionales para emociones visuales (FER2013)
- Integración y comparación de señales multimodales

---

## Requisitos

### Requisitos del Sistema
- Python >= 3.8
- pip (gestor de paquetes de Python)
- Espacio en disco para el modelo pre-entrenado

### Dependencias Principales
- tensorflow >= 2.0.0: Clasificador de imágenes
- numpy >= 1.19.2: Operaciones numéricas
- Pillow >= 8.0.0: Procesamiento de imágenes
- opencv-python >= 4.5.0: Visualización de imágenes (opcional)
- matplotlib >= 3.3.0: Visualización de resultados

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/PabloZuVal/EmotionAnalyzer.git
   cd EmotionAnalyzer
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv emotion_analyzer
   source emotion_analyzer/bin/activate  # En Unix/macOS
   # o
   .\emotion_analyzer\Scripts\activate  # En Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Estructura del Proyecto

```
EmotionAnalyzer/
├── clasificador_texto.py      # Análisis de emociones en texto
├── clasificador_imagen.py     # Análisis de emociones en imágenes
├── comparador_multimodal.py   # Integración y comparación
├── diccionario_emociones.py   # Diccionario para análisis de texto
├── frases.json               # Dataset de frases con emociones
├── imagenes/                 # Directorio de imágenes faciales
│   ├── 01.png
│   ├── 02.png
│   └── ...
├── fer2013_mini_XCEPTION.99-0.65.hdf5  # Modelo pre-entrenado
└── requirements.txt          # Dependencias del proyecto
```

---

## Uso

El sistema se compone de tres módulos principales que pueden ejecutarse independientemente:

1. **Análisis de Texto**:
   ```bash
   python clasificador_texto.py
   ```
   Analiza las frases del archivo `frases.json` usando el diccionario emocional.

2. **Análisis de Imágenes**:
   ```bash
   python clasificador_imagen.py
   ```
   Procesa las imágenes faciales usando el modelo FER2013.

3. **Análisis Multimodal**:
   ```bash
   python comparador_multimodal.py
   ```
   Ejecuta el análisis completo y genera el archivo `resultados.csv`.

---

## Resultados y Métricas

### Clasificador de Texto
- Precisión global: 93.33%
- Manejo efectivo de negaciones y contexto
- Sistema de puntuación basado en números enteros
- Solo 4 casos de error en 60 evaluaciones

### Clasificador de Imágenes
Principales desafíos identificados:
- Confusión frecuente entre emociones similares:
  * Miedo → Sorpresa (7 casos)
  * Asco → Alegría (5 casos)
  * Tristeza → Sorpresa (5 casos)

Mejoras implementadas:
- Umbrales de confianza específicos por emoción
- Sistema de emociones relacionadas
- Normalización mejorada de imágenes
- Lógica de decisión robusta

### Sistema Multimodal
- Tasa de coincidencia: 28.3%
- 17 casos exitosos de 60 evaluaciones
- Documentación detallada en `resultados.csv`

---

## Entregables

1. **Código Fuente**:
   - `clasificador_texto.py`
   - `clasificador_imagen.py`
   - `comparador_multimodal.py`

2. **Archivo de Resultados**:
   - `resultados.csv` con las columnas:
     - frase
     - imagen
     - emocion_texto
     - emocion_imagen
     - emocion_esperada
     - coincide

3. **Informe de Reflexión** (`informe_reflexion.pdf`):
   - Máximo 2 páginas
   - Análisis de resultados
   - Discusión de causas de divergencia
   - Conclusiones y observaciones

---

## Evaluación

| Criterio | Puntos |
|----------|---------|
| Clasificador de texto funcional y preciso | 25 |
| Clasificador de imagen implementado y funcional | 25 |
| Comparación precisa entre ambas emociones | 20 |
| Análisis reflexivo en el informe | 20 |
| Organización, claridad del código y entregables | 10 |
| **Total** | **100** |

---

## Notas Importantes

- El modelo FER2013 espera imágenes de 64x64 píxeles en escala de grises
- El análisis de texto considera negaciones ("no", "nunca", "jamás")
- Las imágenes deben estar nombradas según el formato especificado en `frases.json`
- Los resultados incluyen tanto la emoción detectada como la esperada
- Se recomienda revisar el informe de reflexión para un análisis detallado de las divergencias

### Limitaciones Conocidas
- El clasificador de imágenes muestra dificultades con emociones similares
- La integración multimodal requiere mejoras para aumentar la tasa de coincidencia
- Las condiciones de iluminación pueden afectar el rendimiento del análisis de imágenes

---

Para cualquier consulta o problema, por favor crear un issue en el repositorio o contactar al equipo docente.