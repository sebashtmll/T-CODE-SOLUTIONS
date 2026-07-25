import re
import difflib

# ==========================================
# 1. COMPONENTE IA (Simulación de Fallback)
# ==========================================
def llm_fallback_correction(token_text):
    """
    Simula la consulta a un LLM para tokens ambiguos con umbral < 0.8.
    Prompt interno: "Corrige este token ambiguo en contexto de UnegScript: '{token_text}'"
    """
    # Simulamos que la IA reconoce que "prnt" es "print" a pesar de ser corto
    corrections = {
        "prnt": "print",
        "prnt(":"print",
    }
    return corrections.get(token_text, None)

# ==========================================
# 2. LEXER HÍBRIDO (Regex + Automata + IA)
# ==========================================
class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.suggestions = []
        self.keywords = ["print", "if", "else"]
        
        # Reglas base (Regex)
        self.token_specification = [
            ('NUMBER',   r'\d+'),
            ('STRING',   r'".*?"'),
            ('ID',       r'[A-Za-z]+'),
            ('ASSIGN',   r'='),
            ('GT',       r'>'),
            ('SEMI',     r';'),
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('SKIP',     r'[ \t\n]+'),
            ('MISMATCH', r'.'), 
        ]
        self.regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specification)

    def tokenize(self):
        for mo in re.finditer(self.regex, self.code):
            kind = mo.lastgroup
            value = mo.group()
            
            if kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Caracter inesperado: {value}')
            elif kind == 'ID':
                if value in self.keywords:
                    self.tokens.append(('KEYWORD', value))
                else:
                    # Si no es keyword, verificamos si fue un error tipográfico
                    best_match = None
                    best_ratio = 0
                    
                    for kw in self.keywords:
                        ratio = difflib.SequenceMatcher(None, value, kw).ratio()
                        if ratio > best_ratio:
                            best_ratio = ratio
                            best_match = kw
                    
                    # Lógica de Umbral de Confianza
                    if best_ratio >= 0.8:
                        # Auto-corrección por similitud alta (Ej: pront -> print)
                        self.suggestions.append(f"Sugerencia (Lexer Automático): '{value}' → '{best_match}'")
                        self.tokens.append(('KEYWORD', best_match))
                    elif best_ratio > 0.5 and best_ratio < 0.8:
                        # Fallback a IA si el umbral es menor a 0.8 pero hay indicios
                        ia_correction = llm_fallback_correction(value)
                        if ia_correction:
                            self.suggestions.append(f"Sugerencia (IA Fallback): '{value}' → '{ia_correction}'")
                            self.tokens.append(('KEYWORD', ia_correction))
                        else:
                            self.tokens.append(('ID', value))
                    else:
                        # Es un identificador normal (como 'x')
                        self.tokens.append(('ID', value))
            else:
                self.tokens.append((kind, value))
        return self.tokens, self.suggestions

# ==========================================
# 3. PARSER RECURSIVO DESCENDENTE Y AST
# ==========================================
class ASTNode:
    pass

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self): return f"PrintNode({self.expr})"

class AssignNode(ASTNode):
    def __init__(self, id_name, value):
        self.id_name = id_name
        self.value = value
    def __repr__(self): return f"AssignNode({self.id_name} = {self.value})"

class IfNode(ASTNode):
    def __init__(self, cond, true_branch, false_branch):
        self.cond = cond
        self.true_branch = true_branch
        self.false_branch = false_branch
    def __repr__(self): return f"IfNode(Cond:{self.cond}, True:{self.true_branch}, False:{self.false_branch})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def match(self, expected_kind, expected_value=None):
        token = self.current_token()
        if token and token[0] == expected_kind and (expected_value is None or token[1] == expected_value):
            self.pos += 1
            return token
        return None

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.current_token()
        
        # Parse: print(...)
        if token[0] == 'KEYWORD' and token[1] == 'print':
            self.match('KEYWORD', 'print')
            # Lookahead opcional para paréntesis
            has_paren = self.match('LPAREN')
            expr = self.current_token()[1]
            self.pos += 1 # Consumir expresión
            if has_paren:
                self.match('RPAREN')
            self.match('SEMI')
            return PrintNode(expr)
            
        # Parse: if ... else ...
        elif token[0] == 'KEYWORD' and token[1] == 'if':
            self.match('KEYWORD', 'if')
            cond_var = self.match('ID')[1]
            op = self.match('GT')[1]
            cond_val = self.match('NUMBER')[1]
            cond = f"{cond_var} {op} {cond_val}"
            true_branch = self.parse_statement()
            
            false_branch = None
            if self.current_token() and self.current_token()[1] == 'else':
                self.match('KEYWORD', 'else')
                false_branch = self.parse_statement()
            return IfNode(cond, true_branch, false_branch)
            
        # Parse: Asignación x = 5;
        elif token[0] == 'ID':
            var_name = self.match('ID')[1]
            self.match('ASSIGN')
            value = self.match('NUMBER')[1]
            self.match('SEMI')
            return AssignNode(var_name, value)
            
        self.pos += 1 # Avanzar si hay error para evitar bucles
        return None

# ==========================================
# 4. EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    codigo_erroneo = 'pront x=5; if x>3 prnt(x) else prnt("no")'
    
    print("--- 1. CÓDIGO ORIGINAL ---")
    print(codigo_erroneo, "\n")
    
    # Análisis Léxico
    lexer = Lexer(codigo_erroneo)
    tokens_corregidos, sugerencias = lexer.tokenize()
    
    print("--- 2. SUGERENCIAS GENERADAS POR LA IA / LEXER ---")
    for sug in sugerencias:
        print("-", sug)
    print()
    
    print("--- 3. TOKENS CORREGIDOS ---")
    print(tokens_corregidos, "\n")
    
    # Análisis Sintáctico
    parser = Parser(tokens_corregidos)
    ast = parser.parse()
    
    print("--- 4. ÁRBOL DE SINTAXIS ABSTRACTA (AST) ---")
    for nodo in ast:
        print(nodo)