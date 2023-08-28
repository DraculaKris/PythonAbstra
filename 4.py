class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
       area =  self.base * self.altura
       return area

Resultado = Retangulo(9,12)
print(f'A área do retângulo é {Resultado.area()}')
