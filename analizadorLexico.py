import ply.lex as lex

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'IGUAL_QUE',
    'COMENTARIO',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
)

reserved = {
    'si': 'SI',
    'entonces': 'ENTONCES',
    'mientras': 'MIENTRAS',
    'sino': 'SINO',
    'repite': 'REPITE',
}

tokens = list(tokens) + list(reserved.values())

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL_QUE = r'=='
t_COMENTARIO = r'//.*'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("Token desconocido: '%s'" % t.value)
    t.lexer.skip(1)
    
t_ignore = ' \t\n'

lexer = lex.lex()

'''
with(open('data.txt', 'r')) as file:
    data = file.read()
    lexer.input(data)

with(open('lexico.txt', 'w')) as lexico:
    while(True):
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        lexico.write(str(tok) + '\n')
'''
