# Informe de Reflexión: Análisis Multimodal de Emociones

## 1. Introducción

Este informe presenta una reflexión detallada sobre el desarrollo y resultados del sistema de reconocimiento multimodal de emociones, que integra análisis de texto en español y reconocimiento de expresiones faciales. El proyecto se desarrolló como parte de la Actividad 2 del curso de Computación Afectiva, con el objetivo de explorar la complejidad de la detección emocional en diferentes modalidades.

## 2. Análisis de Resultados

### 2.1 Rendimiento por Componente

#### Clasificador de Texto
- Precisión global: 93.33% (56/60 casos)
- Fortalezas:
  * Excelente detección de emociones básicas
  * Manejo efectivo de negaciones
  * Sistema robusto de puntuación
- Debilidades:
  * Limitaciones con expresiones ambiguas
  * Dependencia del diccionario predefinido

#### Clasificador de Imágenes
- Precisión: Variable según la emoción
- Principales confusiones:
  * Miedo → Sorpresa (7 casos)
  * Asco → Alegría (5 casos)
  * Tristeza → Sorpresa (5 casos)

### 2.2 Rendimiento Multimodal
- Total de casos analizados: 60
- Coincidencia multimodal: 28.3% (17 casos)
- Divergencia: 71.7% (43 casos)

## 3. Análisis Técnico

### 3.1 Implementación
1. **Procesamiento de Texto**:
   - Uso efectivo del diccionario emocional
   - Preprocesamiento robusto (tokenización, normalización)
   - Sistema de puntuación basado en reglas

2. **Procesamiento de Imágenes**:
   - Modelo FER2013 (64x64 píxeles, escala de grises)
   - Normalización de imágenes
   - Predicción de 7 emociones básicas

### 3.2 Desafíos Técnicos
1. **Texto**:
   - Manejo de contexto limitado
   - Necesidad de lematización más sofisticada
   - Mejora potencial usando modelos de lenguaje

2. **Imágenes**:
   - Sensibilidad a condiciones de iluminación
   - Limitaciones del modelo pre-entrenado
   - Necesidad de mejor preprocesamiento

## 4. Interpretación de Divergencias

### 4.1 Factores Lingüísticos
- La expresión verbal en español tiene matices complejos
- Las negaciones y el contexto afectan la interpretación
- Algunas emociones son más fáciles de expresar textualmente

### 4.2 Factores Visuales
- Las expresiones faciales pueden ser ambiguas
- Limitaciones de imágenes estáticas
- Influencia de factores culturales en la expresión facial

## 5. Propuestas de Mejora

### 5.1 Mejoras Técnicas Inmediatas
1. **Clasificador de Texto**:
   - Implementar lematización con spaCy
   - Expandir el diccionario emocional
   - Mejorar el sistema de puntuación

2. **Clasificador de Imágenes**:
   - Implementar umbrales de confianza
   - Mejorar el preprocesamiento de imágenes
   - Considerar modelos alternativos

### 5.2 Mejoras a Largo Plazo
1. **Sistema Multimodal**:
   - Desarrollar sistema de pesos adaptativos
   - Incorporar análisis de contexto
   - Implementar fusión de modalidades más sofisticada

## 6. Conclusiones

El desarrollo de este sistema multimodal ha proporcionado insights valiosos sobre la complejidad del reconocimiento emocional. El alto rendimiento del clasificador de texto (93.33%) contrasta con los desafíos encontrados en el análisis de imágenes y la integración multimodal.

La tasa de coincidencia del 28.3% en el análisis multimodal, aunque inicialmente puede parecer baja, refleja la complejidad inherente en la expresión emocional humana y los desafíos técnicos en su detección automática. Este proyecto ha demostrado que el reconocimiento efectivo de emociones requiere no solo avances técnicos sino también una comprensión profunda de cómo las emociones se manifiestan en diferentes modalidades.

Las lecciones aprendidas y las mejoras propuestas proporcionan una base sólida para futuras iteraciones del sistema, con un enfoque particular en la mejora de la integración multimodal y la consideración de factores contextuales y culturales.
