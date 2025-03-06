import ply.lex as lex

frase_exemplo = """select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""

tokens = (
    'NUMBER',
    'RPAREN',
    'LPAREN',
    'WHERE',
    'SELECT',
    'ID',
    'A',
    'PREFIXO',
    'SUFIXO',
    'DPONTOS',
    'DOT',
    'STRING',
    'LIMIT',
    'PA',
    'PF',
    'OP'
)

def t_SELECT(t):
    r'select'
    t.type = 'SELECT'
    return t

def t_WHERE(t):
    r'where'
    t.type = 'WHERE'
    return t

def t_LIMIT(t):
    r'LIMIT'
    t.type = 'LIMIT'
    return t

def t_A(t):
    r' a '
    t.type = 'A'
    return t

def t_ID(t):
    r'\?[a-zA-Z]\w*'
    t.type = 'ID'
    return t

def t_PREFIXO(t):
    r'[a-zA-Z]\w*(?=:)'
    return t

def t_SUFIXO(t):
    r':[a-zA-Z]\w*'
    t.value = t.value[1:]  # Remove ':'
    return t

def t_DPONTOS(t):
    r':'
    return t

def t_STRING(t):
    r'"[^"\r\n]*"(?:@[a-zA-Z]+)?'
    return t

def t_NUMBER(t):
    r'\b\d+\b'
    t.value = int(t.value)
    return t

def t_PA(t):
    r'\{'
    return t

def t_PF(t):
    r'\}'
    return t

def t_DOT(t):
    r'\.'
    return t

def t_OP(t):
    r'[=><!]'
    return t

t_ignore = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input(frase_exemplo)

while tok := lexer.token():
    print(tok)