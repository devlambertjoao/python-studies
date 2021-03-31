import numpy as np

n = int(input()) # Numero da coluna 
m = np.arange(1, 145).reshape(12, 12)
soma = m.sum(axis=0)[n]

print("Digite S para Soma ou M para media:")
x = str(input())

def imprimir(valor):
	print("{:.1f}".format(valor))

if x == 'S' or x == 'M':
	imprimir(soma) if x == "S" else imprimir(soma / len(m))
else:
	print("Valor inválido")
