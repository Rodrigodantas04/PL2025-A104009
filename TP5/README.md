# Máquina de Vending

## Autor
Rodrigo Gonçalves Dantas  a104009  
2025-02-28

![Autor](https://github.com/Rodrigodantas04/PL2025-A104009/blob/main/TP1/WhatsApp%20Image%202025-02-13%20at%2022.13.00.jpeg)

## Objetivo
Criar um programa em Python que simule uma máquina de vending, gerenciando estoque, aceitando moedas, dispensando produtos e devolvendo troco, com dados salvos em JSON.

## Explicação
O programa usa ply.lex para ler comandos como MOSTRAR, INSERIR, ESCOLHER, ADICIONAR e SAIR. O estoque é uma lista de dicionários carregada de produtos.json e atualizada ao sair.

MOSTRAR: Lista produtos.
INSERIR: Soma moedas ao saldo.
ESCOLHER: Dispensa produto se houver saldo e estoque.
ADICIONAR: Atualiza o estoque.
SAIR: Devolve troco e salva o estoque.
Erros como saldo insuficiente ou produto inexistente são tratados com mensagens claras


## Conclusão
O programa cumpre o objetivo de simular uma máquina de vending de forma funcional e prática, respeitando todos os requisitos do enunciado. Ele gerencia o estoque corretamente, processa comandos do utilizador com precisão e mantém os dados salvos em JSON entre execuções, o que garante uma experiência contínua. A solução é simples, mas robusta, lidando bem com situações como falta de saldo, stock esgotado ou entradas inválidas. Este trabalho foi uma boa oportunidade para aplicar conceitos de programação como análise léxica, manipulação de arquivos e controle de fluxo, resultando em um sistema que reflete o comportamento real de uma máquina de vendas.
