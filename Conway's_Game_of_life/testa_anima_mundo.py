""" Testa a função anima_mundo do módulo vida. """

from vida.py import *

########################
# testando anima_mundo()
    
print("Se não indicar um ficheiro, será usado um padrão por omissão.")
fich_mundo_inicial = input("Ficheiro com mundo inicial (return para omitir): ")
n = int(input("Quantas iterações? "))
delay = float(input("Qual o atraso desejado (em segundos)? "))

if fich_mundo_inicial == "":
    # criar um mundo conhecido como cruz_largura_7
    mundo_inicial = cria_mundo(11, 11)
    for linha in range(2, 9):
        atribui_valor_celula(mundo_inicial, linha, 5, 1)
    for coluna in range(2, 9):
        atribui_valor_celula(mundo_inicial, 5, coluna, 1)
else:
    # ler o mundo inicial de um ficheiro
    mundo_inicial = le_mundo(fich_mundo_inicial)
    
anima_mundo(n, mundo_inicial, atraso = delay)


