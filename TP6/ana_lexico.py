import ply.lex as lex

tokens = ['NUM', 'PLUS', 'MINUS', 'MULT']

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print("Caractere ilegal:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
