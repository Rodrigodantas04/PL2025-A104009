# Título
Conversor de Markdown para HTML

# Autor
Rodrigo Gonçalves Dantas  a104009 
2025-02-25

![Autor](https://github.com/Rodrigodantas04/PL2025-A104009/blob/main/TP1/WhatsApp%20Image%202025-02-13%20at%2022.13.00.jpeg)

# Objetivo
Criar um programa em Python para converter texto no formato Markdown em HTML, seguindo a sintaxe básica do Markdown. O programa deve processar cabeçalhos (#, ##, ###), negrito (**), itálico (*), links ([texto](url)), imagens e listas numeradas (1., 2., 3.), gerando o código HTML correspondente de forma eficiente, sem dependências externas além da biblioteca padrão do Python.

# Explicação
O programa lê um texto Markdown e o transforma em HTML utilizando expressões regulares para identificar os padrões de formatação. Cabeçalhos são convertidos em tags `<h1>`, `<h2>` e `<h3>`, negrito em `<b>`, itálico em `<i>`, links em `<a>` e imagens em `<img>`. Listas numeradas são organizadas em `<ol>` com `<li>`. O código processa o texto linha a linha, garantindo que todos os elementos sejam transformados corretamente. Um exemplo é incluído no programa, e a saída completa é exibida no terminal. Não há uso de módulos externos além da biblioteca `re`, mantendo a simplicidade e eficiência.

# Resultados
Quanto aos resultados , o meu texto antes da conversão era este:

# Exemplo
Este é um **exemplo** com *itálico* e [link](http://www.uc.pt)
## Segundo nível
Como se vê na imagem: ![coelho](http://www.coelho.com)

1. Primeiro item
2. Segundo item
3. Terceiro item


Resultado da conversão:

<h1>Exemplo</h1>
Este é um <b>exemplo</b> com <i>itálico</i> e <a href="http://www.uc.pt">link</a>
<h2>Segundo nível</h2>
Como se vê na imagem: !<a href="http://www.coelho.com">coelho</a>

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

