# Analisador Léxico 

## Autor
Rodrigo Gonçalves Dantas  a104009  
2025-02-28

![Autor](https://github.com/Rodrigodantas04/PL2025-A104009/blob/main/TP1/WhatsApp%20Image%202025-02-13%20at%2022.13.00.jpeg)

## Objetivo
Criar um analisador léxico para uma linguagem de query, permitindo interpretar e extrair tokens de comandos estruturados. O código implementado utiliza a biblioteca PLY (Python Lex-Yacc) para definir regras de tokenização e processar sentenças de consulta, como a extração de dados de DBPedia.

## Explicação
O analisador léxico identifica elementos essenciais da linguagem de query, como palavras-chave (`SELECT`, `WHERE`, `LIMIT`), identificadores (`?variáveis`), pontuações (`{, }, .`), e strings. Ele faz uso de expressões regulares para definir cada token e trata erros de caracteres inválidos, garantindo um parsing correto da entrada.


## Conclusão
Este analisador léxico fornece uma base sólida para processamento de queries, permitindo futuras expansões para parsing sintático e interpretação semântica. Ele pode ser integrado a sistemas que requerem análise automática de consultas estruturadas. Se houver dúvidas ou sugestões, sinta-se à vontade para contribuir no repositório!

