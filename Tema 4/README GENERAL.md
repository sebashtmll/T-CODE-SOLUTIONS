# Análisis Léxico y Sintáctico: Implementación y Aplicaciones

Este proyecto documenta el estudio y la implementación práctica de las fases iniciales de un compilador, específicamente el análisis léxico y sintáctico, aplicando la teoría de lenguajes formales y autómatas.

## Descripción del Proyecto

El trabajo explora la transformación de código fuente en tokens mediante dos enfoques metodológicos: la implementación manual (utilizando Python) y la automatización mediante metacompiladores (Flex). Además, se analiza el papel de los autómatas de pila en la validación de estructuras sintácticas anidadas y su aplicación crítica en el área de seguridad informática.

## Contenidos Principales

* 
**Análisis Léxico:** Uso de expresiones regulares para la tokenización de lenguajes.


* 
**Análisis Sintáctico:** Implementación de autómatas de pila (PDA) para gestionar recursividad y estructuras anidadas (ej. balanceo de paréntesis).


* **Implementación:**
* 
**Metacompiladores:** Uso de **Flex** para generar analizadores léxicos eficientes.


* 
**Desarrollo Manual:** Script en Python para el procesamiento de archivos de configuración (tipo Docker).




* 
**Seguridad Informática:** Aplicación de analizadores léxicos para la validación de reglas en lenguajes de detección de amenazas como **YARA**.



## Tecnologías Utilizadas

* 
**Lenguajes:** C, Python.


* 
**Herramientas:** Flex (generador de lexers), GCC, Make, MSYS2 (entorno POSIX en Windows).



## Estructura del Repositorio

* 
`/src`: Contiene los archivos de especificación (`.l`), el código fuente en Python y los archivos de configuración (`Makefile`).


* 
`/pruebas`: Ejemplos de archivos de entrada (lenguaje L, Dockerfiles, reglas YARA).



## Autores

* Longart, Daniela 


* Martinez, Fabiana 


* Marquez, Félix 


* Ortiz, Sebastian 


* Valencia, Haddan 



---

Link defensa: https://drive.google.com/file/d/1K2xuUVGy0VuBVM2JhpeMKpIp4cpNf6_X/view?usp=drive_link 
