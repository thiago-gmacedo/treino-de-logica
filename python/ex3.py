# Exercício 3: Faça um programa que, 
# dado um valor n qualquer, tal que n > 1 ,
# imprima na tela um quadrado 
# feito de asteriscos de lado de tamanho n . Por exemplo:

def create_square(side):
  line = side * "*"
  square = str();
  for n in range(side):
    square += f"{line}\n"
  return square

