# Investigación Teórico-Práctica: Lenguajes y Gramáticas Formales

---

##  Integrantes
* **Daniela Longart** - C.I: 31.445.710
* **Fabiana Martínez** - C.I: 30.498.516
* **Sebastián Ortiz** - C.I: 30.576.350
* **Haddan Valencia** - C.I: 31.181.222

---

##  Resumen del Proyecto
Este repositorio contiene una investigación teórico-práctica exhaustiva sobre los fundamentos de los **Lenguajes Formales y las Gramáticas** enfocados en la ingeniería de compiladores. El objetivo central del proyecto es fundamentar rigurosamente los mecanismos de generación sintáctica y aplicar dichos modelos abstractos a la resolución de problemas de optimización de código, simulación algorítmica y reconocimiento de patrones.

El trabajo se desglosa en cuatro componentes esenciales:
1. **Fundamentos y Clasificación:** Análisis de la Jerarquía de Chomsky (Tipo 0 a Tipo 3) y formalización mediante la notación BNF (Backus-Naur Form).
2. **Modelado y Derivación Práctica:** Diseño de una Gramática Libre de Contexto (GLC) restrictiva sobre el alfabeto Sigma = \{a,c,g,t\} para la generación de estructuras geométricas (cuadrados, cubos) y orgánicas (árboles).
3. **Higiene y Optimización Gramatical:** Resolución algorítmica de patologías que degradan el rendimiento de un *parser*, tales como la ambigüedad, la recursividad por la izquierda y la factorización por la izquierda.
4. **Reconocimiento de Patrones y Autómatas:** Modelado de expresiones regulares (Regex) y construcción de Autómatas Finitos Determinísticos (AFD) para la validación de jugadas en un subconjunto simplificado de la notación PGN (Portable Game Notation) de ajedrez.

---

##  Implementación en Python (Ejercicios Prácticos)
Para consolidar los conceptos abstractos del informe, este repositorio incluye un conjunto de **ejercicios y scripts desarrollados en Python** que automatizan y demuestran de forma práctica los algoritmos investigados:
* **Simulador de Autómata PGN:** Un motor en Python que implementa las transiciones del AFD diseñado para validar movimientos individuales de ajedrez según las reglas de la expresión regular matemática.
* **Validación Léxica con Regex:** Scripts optimizados que utilizan el módulo `re` de Python para el reconocimiento determinista y rápido de patrones y secuencias de tokens válidas.
* **Modelado de Reglas de Producción:** Algoritmos complementarios que ejemplifican la lógica de sustitución y el comportamiento de las transformaciones gramaticales frente a las patologías analizadas.

---

##  Sustentación en Video
Como parte de la evaluación y defensa práctica de esta investigación, se ha grabado una explicación detallada del funcionamiento de la gramática geométrica, la resolución de las patologías del analizador sintáctico y el recorrido de los estados del autómata PGN.

Puedes ver la defensa del proyecto haciendo clic en el siguiente enlace:

 **https://youtu.be/-BvrTs1oQXg**



##  Contenido del Repositorio
* `/docs`: Contiene el documento bajo formato de informe académico completo (`Lenguajes y gramaticas formales.docx`).
* `/src`: Scripts de Python correspondientes a los ejercicios prácticos de expresiones regulares, validación de cadenas y simulación del AFD de ajedrez.
* `/models`: Ejemplos de ejercicios resueltos en python

---

## Bibliografía Principal
* Aho, A., Lam, M., Sethi, R. y Ullman, J. (2007). *Compilers: Principles, techniques, and tools* (2da ed.). Pearson Addison-Wesley.
* Johnson, M., y Zelenski, J. (2012). *Formal grammars*. Stanford University.
* Moreno, M. (2004). *Elimination of left recursion*. University of Western Ontario.