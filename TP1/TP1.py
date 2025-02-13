import sys

def somadorONOFF(l, estado, res):
    i = 0

    while i < len(l):
        valor = 0

        if l[i:i+2].lower() == "on":
            estado = True
            i += 2

        elif l[i:i+3].lower() == "off":
            estado = False
            i += 3

        elif l[i].isdigit() and estado:
            while i < len(l) and l[i].isdigit():
                valor = valor * 10 + int(l[i])
                i += 1
            res += valor

        elif l[i] == '=':
            print(f"Resultado Atual: {res}")
            i += 1

        else:
            i += 1

    return res, estado

def processar_ficheiro(nome_ficheiro):
    resultado = 0
    state = False

    try:
        with open(nome_ficheiro, 'r') as f:
            for linha in f:
                resultado, state = somadorONOFF(linha.strip(), state, resultado)

        print(f"\nSoma total no ficheiro: {resultado}")

    except FileNotFoundError:
        print(f"Erro: O ficheiro '{nome_ficheiro}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

processar_ficheiro(r"C:\Users\Utilizador\OneDrive\Ambiente de Trabalho\3ºAno\PL\TP1\data.txt")
