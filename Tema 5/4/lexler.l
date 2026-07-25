%{
#include "parser.tab.h"
%}

%%
"services"    { return SERVICES; }
[a-zA-Z_][a-zA-Z0-9_]* { return KEY; }
[0-9]+        { return VALUE; }
":"           { return COLON; }
"-"           { return DASH; }
[ \t\n]+      { /* Ignorar espacios y saltos */ }
.             { return yytext[0]; }
%%
int yywrap() { return 1; }