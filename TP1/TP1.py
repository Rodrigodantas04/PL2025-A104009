import sys

def somadorONOFF(l,estado, res):
    i=0


    while i<len(l):
        valor=0
        if l[i:i+2].lower()=="on" :
            estado=True
            i+=2

        elif l[i:i+3].lower()=="off" :
            estado=False
            i+=3

        elif l[i] in "0123456789" and estado:
            while l[i] in "0123456789":
                valor=valor*10+int(l[i])
                i=i+1
            res+=valor

        elif l[i]=='=':
            print(res)
            i+=1
        else:
            i=i+1
    return res , estado

resultado=0
state=True
for linha in sys.stdin:
    resultado,state= somadorONOFF(linha,state,resultado)