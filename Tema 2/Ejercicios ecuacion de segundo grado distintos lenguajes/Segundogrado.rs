use std::time::Instant;

fn main() {
    let n = 200;
    // Datos de prueba uniformes: a=1, b=-5, c=6 (Raíces reales)
    let a: Vec<f64> = vec![1.0; n];
    let b: Vec<f64> = vec![-5.0; n];
    let c: Vec<f64> = vec![6.0; n];
    let mut resultados: Vec<(f64, f64)> = vec![(0.0, 0.0); n];

    // Iniciamos la medición del tiempo de cálculo
    let inicio = Instant::now();

    for i in 0..n {
        let discriminante = b[i] * b[i] - 4.0 * a[i] * c[i];
        let x1 = (-b[i] + discriminante.sqrt()) / (2.0 * a[i]);
        let x2 = (-b[i] - discriminante.sqrt()) / (2.0 * a[i]);
        resultados[i] = (x1, x2);
    }

    let duracion = inicio.elapsed().as_secs_f64() * 1000.0; // Convertir a ms
    println!("Rust - Tiempo de cálculo: {:.4} ms", duracion);
    
    // Imprimimos el último elemento para evitar que el compilador optimice y elimine el bucle
    println!("Control (Último resultado): x1 = {}, x2 = {}", resultados[n-1].0, resultados[n-1].1);
}