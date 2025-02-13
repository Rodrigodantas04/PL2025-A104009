# Titulo
TP1 - Somador On Off
# Autor
Rodrigo Gonçalves Dantas  a104009 
2025-02-13

![Autor](https://github.com/Rodrigodantas04/PL2025-A104009/blob/main/TP1/WhatsApp%20Image%202025-02-13%20at%2022.13.00.jpeg)

# Objetivo
Criar um programa em Pyrhon - Somador on/off , que some todas as sequenciasde digitos que encontre num texto. Mas com as seguintes indicações:
Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída.

# Explicação
O programa lê um ficheiro de texto e processa digitos com base no estado "ON" ou "OFF", sem usar módulos externos. Quando o estado está "ON", os digitos encontrados são somados; quando está "OFF", são ignorados. O estado alterna ao encontrar "On" ou "Off", e sempre que aparece "=", a soma parcial é impressa. O código mantém o estado global ao longo do ficheiro, garantindo que a soma seja acumulada corretamente. Caso o ficheiro não exista, é gerado um erro. No final, a soma total dos números processados enquanto o estado esteve "ON" é apresentada.

# Resultados
Resultado parcial: 25
Resultado parcial: 77
Resultado parcial: 142
Resultado parcial: 374

Soma total no ficheiro: 395
