%{
#include <stdio.h>
%}

%option noyywrap

%%

"fn"        { printf("TOKEN: KW_FN, Lexema: %s\n", yytext); }
"let"       { printf("TOKEN: KW_LET, Lexema: %s\n", yytext); }
"mut"       { printf("TOKEN: KW_MUT, Lexema: %s\n", yytext); }
"if"        { printf("TOKEN: KW_IF, Lexema: %s\n", yytext); }
"else"      { printf("TOKEN: KW_ELSE, Lexema: %s\n", yytext); }
"return"    { printf("TOKEN: KW_RETURN, Lexema: %s\n", yytext); }

"i32"|"f64"|"bool" { printf("TOKEN: TIPO_DATO, Lexema: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("TOKEN: IDENTIFICADOR, Lexema: %s\n", yytext); }

[0-9]+"."[0-9]+ { printf("TOKEN: NUM_DECIMAL, Lexema: %s\n", yytext); }
[0-9]+      { printf("TOKEN: NUM_ENTERO, Lexema: %s\n", yytext); }

"="         { printf("TOKEN: OP_ASIGNACION, Lexema: %s\n", yytext); }
"+"|"-"|"*"|"/" { printf("TOKEN: OP_ARITMETICO, Lexema: %s\n", yytext); }
"=="|"!="|">"|"<"|">="|"<=" { printf("TOKEN: OP_RELACIONAL, Lexema: %s\n", yytext); }

"{"|"}"|"("|")"|";"|":"|"," { printf("TOKEN: SIMBOLO, Lexema: %s\n", yytext); }

[ \t\n\r]+  { /* Ignorar espacios, tabulaciones y saltos de linea */ }
"//".* { /* Ignorar comentarios de una linea */ }

.           { printf("ERROR LEXICO: Caracter no reconocido: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error al abrir el archivo");
            return 1;
        }
        yyin = file;
    } else {
        printf("Por favor, indique el archivo de entrada. Ejemplo: ./Lexl codigo.rs\n");
        return 1;
    }
    
    yylex();
    return 0;
}