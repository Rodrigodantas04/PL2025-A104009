import re


def md_to_web(txt):
    txt = re.sub(r'^# (.+)$', r'<h1>\1</h1>', txt, flags=re.M)  # cabeçalho 1
    txt = re.sub(r'^## (.+)$', r'<h2>\1</h2>', txt, flags=re.M)  # cabeçalho 2
    txt = re.sub(r'^### (.+)$', r'<h3>\1</h3>', txt, flags=re.M)  # cabeçalho 3

    txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', txt)  # negrito
    txt = re.sub(r'\*(.+?)\*', r'<i>\1</i>', txt)  # itálico
    txt = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', txt)  # link
    txt = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', txt)  # imagem

    linhas = txt.split('\n')
    lista_ativa = False
    resultado = []
    for ln in linhas:  # listas numeradas
        if re.match(r'^\d+\.\s', ln):
            if not lista_ativa:
                resultado.append('<ol>')
                lista_ativa = True
            resultado.append(re.sub(r'^\d+\.\s(.+)$', r'<li>\1</li>', ln))
        else:
            if lista_ativa:
                resultado.append('</ol>')
                lista_ativa = False
            resultado.append(ln)
    if lista_ativa:
        resultado.append('</ol>')

    return '\n'.join(resultado)


texto = """
# Exemplo
Este é um **exemplo** com *itálico* e [link](http://www.uc.pt)
## Segundo nível
Como se vê na imagem: ![coelho](http://www.coelho.com)

1. Primeiro item
2. Segundo item
3. Terceiro item
"""

saida = md_to_web(texto)
print(saida)