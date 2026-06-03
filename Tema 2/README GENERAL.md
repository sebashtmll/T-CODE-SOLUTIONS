```markdown
# Tema 2  - Los lenguajes de programación

**Asignatura:** Lenguaje y Compiladores 
**Universidad:** Universidad Nacional Experimental de Guayana (UNEG)  
**Sección:** 01  
**Docente:** Félix Márquez  

---

##  Descripción General del Proyecto

Este repositorio contiene el trabajo de investigación correspondiente al **Tema 2: Los lenguajes de programación** de la asignatura. El objetivo principal es analizar los lenguajes de programación no solo como herramientas estáticas, sino como productos de software con arquitecturas orientadas a fines específicos y restricciones formales rigurosas.

El proyecto se desarrolla en tres grandes actividades:

1. **Análisis de paradigmas de programación** (Imperativo, OO, Funcional, Lógico, Concurrente).
2. **Estudio morfológico, sintáctico y benchmarking** de cuatro lenguajes (Zig, Python, Rust, JavaScript).
3. **Diseño de un Lenguaje de Dominio Específico (DSL)** llamado *Lenguaje L* para la gestión de una microred eléctrica inteligente (ECO-GRID).

---

##  Actividad I: Análisis de Paradigmas

**¿De qué trata?**  
Se elabora un marco analítico donde se explican en detalle los paradigmas clásicos y emergentes de la programación, incluyendo:

- Imperativo/Estructural
- Orientado a Objetos
- Funcional
- Lógico/Declarativo
- Concurrente/Actores

Además, se documenta el fenómeno de **convergencia multiparadigma** en lenguajes modernos.  

---

##  Actividad II: Estudio Morfológico, Sintáctico y Benchmarking

**¿De qué trata?**  
Se seleccionan cuatro lenguajes con enfoques tecnológicos diferenciados:

- **Zig** (sistemas, compilación nativa)
- **Python** (alto nivel, interpretado)
- **Rust** (seguridad de memoria, compilación nativa)
- **JavaScript** (dinámico, JIT en V8)

Para cada uno se realiza:

1. **Análisis morfológico (léxico):** tokens, palabras reservadas, identificadores, literales e indentación.
2. **Análisis sintáctico:** estructuras de control (bucles, condicionales, subprogramas).
3. **Benchmarking:** se ejecuta un algoritmo de carga intensiva (ej. conjetura de Collatz, cálculo de ecuaciones o simulación de blockchain) midiendo tiempo de ejecución y consumo de memoria.

---

##  Actividad III: Diseño de un DSL para ECO-GRID (Lenguaje L)

**¿De qué trata?**  
Se diseña un **Lenguaje de Dominio Específico (DSL)** llamado *Lenguaje L* para operar una microred eléctrica inteligente (ECO-GRID). El sistema simulado incluye:

- Paneles solares y turbinas eólicas
- Bancos de baterías de litio
- Sensores de flujo y temperatura
- Relés de alta potencia

**Componentes definidos del Lenguaje L:**

- Alfabeto y reglas léxicas (tokens, delimitadores, literales)
- Palabras clave obligatorias (`init_grid`, `leer_temperatura`, `estado_carga`, `conmutar_linea`, `si...entonces...fin_si`, `mientras...ejecutar...fin_mientras`)
- Gramática sintáctica abstracta

**Dos escenarios operativos codificados en Lenguaje L:**

1. **Escenario A – Prevención de fuga térmica:**  
   Monitoreo continuo de temperatura, activación de refrigeración, desconexión de carga solar y desvío a red comercial.

2. **Escenario B – Balance de carga y optimización energética:**  
   Evaluación del estado de baterías y generación solar para vender excedentes a la red o aislar sectores no críticos.

---

## Defensas Individuales (Evaluación Oral)

**Formato:**  
Cada integrante del equipo grabó un video de **maximo 10 minutos** donde:

- Expone y justifica conceptualmente una de las actividades.
- Explica el funcionamiento lógico-sintáctico del código escrito.
- Responde implicaciones del compilador/intérprete sobre el lenguaje seleccionado.
-Enlace del video: https://youtu.be/qU_UiE1TpaE 



---

##  Informe Final

El informe en PDF realiza el desglose y explicación de cada una de las 3 actividades, otorgando definiciones y los códigos de ejecución.

---

## Integrantes del Equipo

| Nombre | Cédula |
|--------|--------|
| Longart, Daniela | V-31445710 |
| Martínez, Fabiana | V-30498516 |
| Ortiz, Sebastián | V-30576350 |
| Valencia, Haddan | V-31818222 |

---


Para cualquier consultad, favor contactar a los integrantes del equipo.

--- 

```
