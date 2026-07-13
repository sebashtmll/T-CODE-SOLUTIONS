%{
#include <stdio.h>
%}

%option noyywrap

%%
"let"           { printf("TOKEN_LET\n"); }
"fn"            { printf("TOKEN_FN\n"); }
"if"            { printf("TOKEN_IF\n"); }
[0-9]+          { printf("TOKEN_NUMERO(%s)\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("TOKEN_ID(%s)\n", yytext); }
"="             { printf("TOKEN_ASIGNACION\n"); }
";"             { printf("TOKEN_PUNTO_COMA\n"); }
[ \t\n]+        { /* Ignorar espacios */ }
.               { printf("TOKEN_DESCONOCIDO(%s)\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}