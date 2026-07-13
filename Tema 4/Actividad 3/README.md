#ACTIVIDAD 3: Analizador Léxico para Subconjunto de Rust (Lenguaje L)

Este repositorio contiene la implementación de un analizador léxico (lexer) diseñado para tokenizar un subconjunto específico del lenguaje de programación Rust. Ha sido construido utilizando la herramienta de metacompilación **Flex** y el compilador **GCC**.

## 1. Requisitos Previos e Instalación

Para compilar y ejecutar este lexer, necesitas tener instalados `flex` y `gcc` en tu entorno (preferiblemente Linux/Debian/Ubuntu).

Abre tu terminal y ejecuta el siguiente comando para instalar las dependencias:

```bash
sudo apt-get update
sudo apt-get install flex gcc