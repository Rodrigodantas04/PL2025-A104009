from ana_lexico import lexer

prox_token = ('Erro', '', 0, 0)

def erro_sintatico(token):
    print("Erro de sintaxe, token inesperado:", token)

# Avança para o próximo token do lexer
def consumir_token(esperado):
    global prox_token
    if prox_token.type == esperado:
        prox_token = lexer.token()
    else:
        erro_sintatico(prox_token)

# Processa fatores (números)
def analisar_fator():
    global prox_token
    if prox_token.type == 'NUM':
        valor = int(prox_token.value)
        consumir_token('NUM')
        return valor
    else:
        erro_sintatico(prox_token)
        return 0

# Processa termos (multiplicação)
def analisar_termo():
    global prox_token
    resultado = analisar_fator()
    while prox_token and prox_token.type == 'MULT':
        consumir_token('MULT')
        resultado *= analisar_fator()
    return resultado

# Processa expressões completas (+ e - com menor precedência que *)
def analisar_expressao():
    global prox_token
    resultado = analisar_termo()
    while prox_token and prox_token.type in ['PLUS', 'MINUS']:
        if prox_token.type == 'PLUS':
            consumir_token('PLUS')
            resultado += analisar_termo()
        elif prox_token.type == 'MINUS':
            consumir_token('MINUS')
            resultado -= analisar_termo()
    return resultado

# Inicia a análise sintática
def iniciar_parser(entrada):
    global prox_token
    lexer.input(entrada)
    prox_token = lexer.token()
    resultado = analisar_expressao()
    print("Resultado:", resultado)
    return resultado
