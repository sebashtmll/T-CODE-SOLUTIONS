fn main() {
    println!("Hello, world!");
}
use pest_derive::Parser;

#[derive(Parser)]
#[grammar = "grammar.pest"] // Aqui se vincula el archivo anterior
pub struct LParser;

fn main() {
    let codigo = "fn main { let x = 10 + 5; }";
    let pairs = LParser::parse(Rule::programa, codigo).unwrap();
    // Recorre los pares para ver cómo los clasificó el lexer
}

use pest::Parser;
use pest_derive::Parser;

#[derive(Parser)]
#[grammar = "grammar.pest"]
struct LParser;

fn main() {
    // Código de prueba que sigue las reglas de tu lenguaje L
    let input = "fn main { let x = 10 + 5; }";

    // Intentamos parsear la entrada usando la regla "programa"
    match LParser::parse(Rule::programa, input) {
        Ok(pairs) => {
            println!("Lexer exitoso. Tokens detectados:");
            // Iteramos sobre todos los elementos encontrados
            for pair in pairs.flatten() {
                println!("Token: {:?}, Valor: '{}'", pair.as_rule(), pair.as_span().as_str());
            }
        }
        Err(e) => {
            eprintln!("Error en el análisis léxico/sintáctico: {}", e);
        }
    }
}