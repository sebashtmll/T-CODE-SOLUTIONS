%{
#include <stdio.h>
void yyerror(const char *s) { printf("Error sintáctico: %s\n", s); }
int yylex();
%}

%token SERVICES KEY VALUE COLON DASH

%%
// Traducción de la lógica de estructura de Docker
document : SERVICES COLON block ;

block    : KEY COLON content_block ;

content_block : KEY 
              | DASH KEY 
              | content_block content_block ;
%%

int main() {
    yyparse();
    return 0;
}