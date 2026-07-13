# Proyecto: Analizador Léxico para Lenguaje L (Subconjunto de Rust)

## 1. Descripción del Proyecto
Este proyecto implementa un analizador léxico (**lexer**) para el "Lenguaje L", un subconjunto minimalista de Rust. El objetivo es convertir una entrada de texto en tokens reconocibles siguiendo las reglas definidas en el metacompilador.

## 2. Manual de Usuario: Flex (Metacompilador)
**Flex** (*Fast Lexical Analyzer Generator*) es un metacompilador que automatiza la creación de analizadores léxicos.
* **Función**: Traduce una especificación de reglas (expresiones regulares) escrita en un archivo `.l` a código fuente en lenguaje C (`lex.yy.c`).
* **Ventaja**: Permite definir gramáticas de forma modular y eficiente, delegando a la herramienta la generación de la lógica de reconocimiento de patrones.


## 3. Descripción del Lenguaje L
El Lenguaje L reconoce los siguientes tokens:
* **Palabras clave**: `let`, `fn`, `if`.
* **Identificadores**: Nombres de variables y funciones.
* **Literales**: Números enteros.
* **Operadores/Símbolos**: `=`, `;`.
* **Ignorados**: Espacios, tabulaciones y saltos de línea.

## 4. Proceso de Implementación
### Requisitos
* Entorno **MSYS2** (con entorno UCRT64).
* Paquetes: `flex`, `gcc`, `make`.

### Instalación y Compilación
1. **Instalar dependencias** (en MSYS2 terminal):
   ```bash
   pacman -S mingw-w64-ucrt-x86_64-gcc flex make

* En la raiz del proyecto se debe ejecutar el comando make
* Posterior a la ejecucion del comando make colocar: echo "let x = 10;" > test.txt

Además de la implementación con Flex, se desarrolló un analizador léxico en Python para demostrar la lógica de tokenización mediante expresiones regulares.

### Explicación Técnica
***El script lexer.py*** implementa un analizador léxico funcional basado en la detección de patrones. Sus componentes principales son:

1. Motor de RegEx: Utiliza re.finditer para recorrer el archivo de entrada y clasificar el texto en categorías como instrucciones, argumentos, comentarios o errores.

2. Procesamiento de Flujo: Gracias al uso de yield (generadores), el lexer es altamente eficiente en memoria, ya que procesa el archivo token por token.

3. Gestión de Errores y Contexto: El lexer realiza un seguimiento preciso de la posición (line_num y column), lo que permite identificar y reportar exactamente dónde ocurre un MISMATCH (carácter no reconocido), mejorando significativamente la experiencia de depuración.