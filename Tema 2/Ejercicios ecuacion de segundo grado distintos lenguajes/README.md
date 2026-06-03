# Benchmarking: Ecuaciones de Segundo Grado en Múltiples Lenguajes

Este repositorio contiene un experimento práctico de **benchmarking de software** diseñado para comparar el rendimiento, la eficiencia y la variación sintáctica entre cuatro lenguajes de programación con diferentes filosofías de diseño: **Python, JavaScript (Node.js), Rust y Zig**.

El experimento consiste en resolver de forma vectorial una ecuación de segundo grado $ax^2 + bx + c = 0$ utilizando la fórmula general para un tamaño de muestra de $n = 200$ elementos.

---

## Autores del Proyecto
* **Longart, Daniela** — V-31445710
* **Martínez, Fabiana** — V-30498516
* **Ortiz, Sebastián** — V-30576350
* **Valencia, Haddan** — V-31818222

---

##  Contenido del Repositorio

* **`informe/`**: Carpeta que contiene el informe técnico detallado con las conclusiones, análisis de la arquitectura de los lenguajes (JIT vs. Intérpretes vs. AOT) y las tablas comparativas de hardware.
* **`Segundogrado.py`**: Código fuente en Python  enfocado en la legibilidad sintáctica y la sencillez.
* **`Segundogrado.js`**: Código fuente en JavaScript  utilizando arreglos tipados (`Float64Array`) para optimizar el uso de la memoria en motores V8.
***`Segundogrado.rs`**: Código fuente en Rust  con enfoque en la seguridad de memoria y rendimiento nativo.
***`Segundogrado.zig`**: Código fuente en Zig  que implementa la lógica mediante asignadores manuales de memoria (`page_allocator`).

---

## Video de la Exposición
Puedes ver la defensa del proyecto, el análisis de la sintaxis y la explicación de los resultados en el siguiente enlace de YouTube:
https://youtu.be/qU_UiE1TpaE aquí está el video

---

## Requisitos para la Ejecución

Para ejecutar los archivos de este repositorio en tu máquina local, necesitarás los siguientes entornos:

1.  **Python 3.x**: Descargable desde [python.org](https://www.python.org/).
2.  **Node.js**: Entorno de ejecución para JavaScript, disponible en [nodejs.org](https://nodejs.org/).
3.  **Rust & Cargo**: Cadena de herramientas oficial de Rust, instalable desde [rustup.rs](https://rustup.rs/).
4.  **Zig Compiler**: Compilador nativo de Zig, disponible en [ziglang.org](https://ziglang.org/).
5.   El compilador de Rust requiere las **Herramientas de compilación de Visual C++ (Build Tools)** junto con la opción de desarrollo para el escritorio con C++.

---

##  Instrucciones de Ejecución

Abre una terminal o consola de comandos en la ruta raíz del repositorio y ejecuta el comando correspondiente al lenguaje que deseas auditar:

### Python
Para ejecutar el script interpretado por la consola:
```bash
python Segundogrado.py

### JavaScript (Node.js)
Para ejecutar el código en el entorno Node.js:
```bash
node Segundogrado.js
``` 
###  Rust
Para compilar y ejecutar el código en Rust:
```bash
cd Segundogrado.rs
cargo run
```

###  Zig
Para compilar y ejecutar el código en Zig:
```bash
cd Segundogrado.zig
zig build-exe Segundogrado.zig
./Segundogrado
```
