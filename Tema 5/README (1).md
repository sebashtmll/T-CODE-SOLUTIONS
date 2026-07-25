# Análisis Sintáctico - Compiladores (UNEG)


##  Descripción del Proyecto
Este repositorio contiene el desarrollo integral de la unidad curricular **Lenguajes y Compiladores** de la **Universidad Nacional Experimental de Guayana (UNEG)**. El proyecto aborda la fase teórica y práctica del **Analisis Sintactico (Parsing)**, explorando desde los fundamentos formales de los Arboles de Sintaxis Abstracta (AST), gramáticas LL y LR, hasta la implementacion de parsers y experimentos de rendimiento (benchmarking) en multiples lenguajes de programación (**Python, Java y C**) para procesar archivos de configuración de infraestructura (Docker Compose), culminando en el diseño conceptual de analizadores híbridos deterministas asistidos por Inteligencia Artificial.

---

##  Autores y Datos Académicos
* **Institución:** Universidad Nacional Experimental de Guayana (UNEG)
* **Proyecto de Carrera:** Ingeniería en Informática
* **Unidad Curricular:** Lenguajes y Compiladores
* **Profesor:** Félix Márquez
* **Autores:**
  * Longart, Daniela (`V-31.445.710`)
  * Martínez, Fabiana (`V-30.498.516`)
  * Ortiz, Sebastián (`V-30.576.350`)
  * Valencia, Haddan (`V-31.818.222`)
* **Fecha de Presentación:** Ciudad Guayana, 24 de julio de 2026.

---

##  Contenido y Estructura del Trabajo
El proyecto está estructurado en módulos que cubren tanto los fundamentos teóricos como los desafíos prácticos de programación:

1. **Actividad I: Árbol de Sintaxis Abstracta (AST)**
   * Estudio de la representación jerárquica y optimización del código fuente.
   * Comparativa detallada entre el Árbol de Análisis Concreto (CST) y el Árbol de Sintaxis Abstracta (AST).
   * Implementación de un recorrido mediante patrón *Visitor* en Python para expresiones aritméticas y estructuras condicionales.

2. **Actividad II: Análisis LL y LR**
   * Contraste metodológico entre los analizadores descendentes predictivos (`LL(k)`) y los ascendentes basados en reducción (`LR(k)`).
   * Demostración paso a paso de la derivación descendente y la reducción ascendente sobre un lenguaje formal común ($L$).

3. **Actividad III: Generadores de Analizadores y Gestión de Errores**
   * Uso de metacompiladores y herramientas automatizadas (Bison, ANTLR).
   * Análisis de estrategias formales de recuperación de errores: *Modo de pánico*, *Nivel de frase*, *Producciones de error* y *Corrección global*.

4. **Desafíos 4 y 5: Benchmarking y Parsers Multi-lenguaje (Docker Compose)**
   * **Python:** Implementación con PLY, medición de rendimiento con `time.perf_counter()` y generación automática de reportes gráficos con `Matplotlib`.
   * **Java:** Comparativa de rendimiento entre parsing basado en expresiones regulares y parsing manual línea por línea utilizando búferes eficientes.
   * **C:** Optimización a nivel de punteros de memoria para el procesamiento de archivos YAML de infraestructura de red.

---

## 🚀 Enlace de la Defensa
> 🔗 **Acceso al video de la defensa del proyecto:**
## 🛠️ Requisitos e Instalación
Para ejecutar los experimentos de rendimiento y los analizadores incluidos en el repositorio, asegúrate de tener instalado:
* **Python 3.10+** (Librerías requeridas: `matplotlib`, `ply`)
* **JDK 17+** (Para el módulo de Java)
* **GCC / Clang** (Para el módulo de C)
