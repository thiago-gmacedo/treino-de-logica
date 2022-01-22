# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" .

def verify_length(names):
  higher = str()
  for name in names:
    if len(name) > len(higher):
      higher = name
  return higher

print(verify_length(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))
