# Bloque 3: Higiene y Optimización de Gramáticas

## 📋 Descripción

Este proyecto implementa la demostración de **tres patologías comunes en gramáticas formales** que causan errores en los compiladores, junto con sus respectivas soluciones.

Corresponde al **Bloque 3** de la asignatura *Lenguaje y Compiladores* (UNEG - Ingeniería en Informática).

## 📁 Estructura del Proyecto
bloque3-gramaticas/
├── ambiguedad.py # Caso (a): Gramática ambigua
├── recursividad_izquierda.py # Caso (b): Recursividad por izquierda
├── factorizacion_izquierda.py # Caso (c): Factorización por izquierda
├── main.py # Ejecuta todas las demostraciones
└── README.md # Este archivo


## 🎯 Requisitos Cumplidos

|                      Requisito                                 |           Archivo            | Estado |
|----------------------------------------------------------------|------------------------------|--------|
| Gramática ambigua con dos árboles de derivación distintos      |     `ambiguedad.py`          |   ✅  |
| Algoritmo paso a paso para eliminar recursividad por izquierda |    `recursividad_iz.py`      |   ✅  |
|     Factorización por izquierda con gramática optimizada       |    `factorizacion_iz.py`     |   ✅  |

## 🔧 Requisitos Técnicos

- **Python 3.6 o superior**
- No requiere bibliotecas externas (solo módulos estándar)

## ▶️ Cómo Ejecutar

### Opción 1: Ejecutar todas las demostraciones
```bash
python main.py