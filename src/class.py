


# pessoa = Pessoa("Fernando sozo", 18, 100)

# # print(a.idade)

class Circulo:                       # Classes tem que ser com a primeira letra em maiusculo
  def __init__(self, raio:float):    # Funçoes     == metodos
    self.raio = raio                 # "Variaveis" == propriedades

  def calcular_area(self, pi:float):
    return self.raio * self.raio * pi
  
  def calcular_metade_da_area(self):
    return self.calcular_area(3.1415)/2

circulo = Circulo(10)
print(circulo.calcular_area(3.1415))
print(circulo.calcular_metade_da_area())


