const n = 200;
const a = new Float64Array(n).fill(1.0);
const b = new Float64Array(n).fill(-5.0);
const c = new Float64Array(n).fill(6.0);
const resultados_x1 = new Float64Array(n);
const resultados_x2 = new Float64Array(n);

const inicio = performance.now();

for (let i = 0; i < n; i++) {
    const disc = b[i] * b[i] - 4.0 * a[i] * c[i];
    resultados_x1[i] = (-b[i] + Math.sqrt(disc)) / (2.0 * a[i]);
    resultados_x2[i] = (-b[i] - Math.sqrt(disc)) / (2.0 * a[i]);
}

const fin = performance.now();
console.log(`JavaScript - Tiempo de cálculo: ${(fin - inicio).toFixed(4)} ms`);
console.log(`Control (Último resultado): x1 = ${resultados_x1[n-1]}, x2 = ${resultados_x2[n-1]}`);