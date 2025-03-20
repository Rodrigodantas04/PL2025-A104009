## Autor
Rodrigo Gonçalves Dantas  a104009  
2025-02-28

![Autor](https://github.com/Rodrigodantas04/PL2025-A104009/blob/main/TP1/WhatsApp%20Image%202025-02-13%20at%2022.13.00.jpeg)

## Descrição
Este projeto implementa um analisador sintático para processar expressões matemáticas simples, suportando os operadores de adição (+), subtração (-) e multiplicação (*). O código segue a precedência correta das operações, garantindo que multiplicações sejam processadas antes de somas e subtrações.

Além disso, o projeto inclui um analisador léxico para identificar tokens na entrada e um analisador sintático que avalia as expressões e retorna o resultado.

## Estrutura de Código
O código está dividido em três principais componentes:

# 1. Analisador Léxico 

O lexer identifica os tokens na expressão matemática e os categoriza como:

NUM: Representa números inteiros.
PLUS: Representa o operador de adição (+).
MINUS: Representa o operador de subtração (-).
MULT: Representa o operador de multiplicação (*).

# 2. Analisador Sintático 

O parser analisa a sequência de tokens e processa a expressão conforme as regras de precedência:

Funções Principais:

erro_sintatico(token): Exibe um erro quando um token inesperado é encontrado.
consumir_token(esperado): Verifica se o próximo token é o esperado e avança na análise.
analisar_fator(): Processa números inteiros.
analisar_termo(): Processa multiplicações.
analisar_expressao(): Processa a expressão completa considerando a precedência dos operadores.
iniciar_parser(entrada): Função principal que inicializa o lexer e executa a análise sintática.

# 3. Execução do Programa

O programa principal recebe a expressão do usuário, passa para o lexer e parser, e exibe o resultado calculado.
