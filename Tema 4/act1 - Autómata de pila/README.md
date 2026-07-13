# Autómata de Pila - Validador de Expresiones

## Actividad 1 del Tema 4: Análisis Léxico

Este programa implementa un **Autómata de Pila (PDA - Pushdown Automaton)** para validar el balanceo y anidamiento correcto de paréntesis `()`, corchetes `[]` y llaves `{}` en expresiones matemáticas.

El programa simula las operaciones fundamentales de un autómata de pila:
- **SHIFT**: Guardar símbolos de apertura en la pila
- **REDUCE/POP**: Verificar y eliminar símbolos de cierre
- **IGNORAR**: Omitir caracteres que no afectan la estructura

> **Regla LIFO**: *Último en entrar, primero en salir*

---

## Características

- Validación paso a paso de expresiones
- Visualización clara del estado de la pila en cada operación
- Detección de errores con mensajes descriptivos
- Aceptación por **pila vacía** (criterio teórico de PDA)
- Interfaz interactiva en consola
- Soporte para paréntesis, corchetes y llaves

---

## Ejecutar el programa
python automataPila.py