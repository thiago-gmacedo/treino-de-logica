from array import array


# Crie uma função que receba dois números e retorne o maior deles.

def maior(valor1, valor2):
  lista = [valor1, valor2]
  lista.sort()
  return lista[1]
