# pyrefly: ignore [missing-import]
import ply.lex as lex

# Definición de los tokens que utilizará el parser
tokens = ('SERVICES', 'KEY', 'VALUE', 'COLON', 'DASH', 'NEWLINE', 'INDENT', 'DEDENT')

class LexToken:
    def __init__(self, type, value, lineno, lexpos):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.lexpos = lexpos

    def __repr__(self):
        return f"LexToken({self.type},{repr(self.value)},{self.lineno},{self.lexpos})"

class IndentLexer:
    def __init__(self):
        self.tokens = tokens
        self.token_queue = []
        self.current_token_idx = 0

    def input(self, data):
        self.token_queue = []
        self.current_token_idx = 0
        lines = data.split('\n')
        indent_levels = [0]

        for line_num, line in enumerate(lines, 1):
            # Eliminar comentarios de tipo YAML (#)
            if '#' in line:
                line = line.split('#', 1)[0]

            stripped = line.strip()
            # Omitir líneas vacías
            if not stripped:
                continue

            # Calcular la indentación (cantidad de espacios al principio de la línea)
            indent = len(line) - len(line.lstrip(' '))

            # Comparar el nivel de indentación actual con la pila
            current_indent = indent_levels[-1]
            if indent > current_indent:
                indent_levels.append(indent)
                self.token_queue.append(LexToken('INDENT', ' ' * (indent - current_indent), line_num, indent))
            elif indent < current_indent:
                while indent < indent_levels[-1]:
                    indent_levels.pop()
                    self.token_queue.append(LexToken('DEDENT', '', line_num, indent))
                if indent != indent_levels[-1]:
                    raise SyntaxError(f"Error de indentación en línea {line_num}: se esperaba nivel {indent_levels[-1]}, obtenido {indent}")

            # Procesar el contenido de la línea
            if stripped.startswith('-'):
                # Es un elemento de lista
                dash_pos = line.find('-')
                self.token_queue.append(LexToken('DASH', '-', line_num, dash_pos))
                val = stripped[1:].strip()
                # Quitar comillas si están presentes
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                val_pos = line.find(val) if val else dash_pos + 1
                self.token_queue.append(LexToken('VALUE', val, line_num, val_pos))
            elif ':' in stripped:
                # Es un par clave-valor o una cabecera de bloque
                key, val = stripped.split(':', 1)
                key = key.strip()
                val = val.strip()

                # Identificar si la clave es la palabra reservada 'services'
                token_type = 'SERVICES' if key == 'services' else 'KEY'
                self.token_queue.append(LexToken(token_type, key, line_num, line.find(key)))
                self.token_queue.append(LexToken('COLON', ':', line_num, line.find(':')))

                if val:
                    # Quitar comillas si están presentes
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    self.token_queue.append(LexToken('VALUE', val, line_num, line.find(val)))
            else:
                # Si no tiene '-' ni ':', es un valor suelto o texto
                val = stripped
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                self.token_queue.append(LexToken('VALUE', val, line_num, line.find(val)))

            # Añadir token NEWLINE al final de cada línea no vacía procesada
            self.token_queue.append(LexToken('NEWLINE', '\n', line_num, len(line)))

        # Emitir tokens DEDENT restantes al final del archivo
        while len(indent_levels) > 1:
            indent_levels.pop()
            self.token_queue.append(LexToken('DEDENT', '', len(lines), 0))

    def token(self):
        if self.current_token_idx < len(self.token_queue):
            tok = self.token_queue[self.current_token_idx]
            self.current_token_idx += 1
            return tok
        return None

# Instancia del lexer por defecto para compatibilidad
lexer = IndentLexer()