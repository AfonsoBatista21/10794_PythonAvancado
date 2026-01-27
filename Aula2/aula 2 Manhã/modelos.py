class carro:
    def __init__(self, marca :str, modelo):
        self.marca = marca.title()
        self.modelo = modelo.title()


"""
assuma que o carro se desloca a uma velocidade constante 

a velocidade deve ser expressa em km/h
o tempo em minutos

a função deve atualizar o num_km do carro
"""
def mover(self, velocidade: float, tempo: float):
    distancia = (velocidade * tempo) / 60
    self.num_km += distancia
#calcule o consumo de combustivel total do carro
#assuma que o consume e constatente (x l por km)
# define o x onde fizer mais sentido
def calcular_combustivel(self, consumo: float):
    total_combustivel = self.num_km * consumo
    return total_combustivel


# crie a class livro (defina apenas os atributos)
class livro:
    def __init__(self, titulo: str, autor: str, ano: int = None, editora: str = None, isbn: str = None,):
        self.titulo = titulo.title()
        self.autor = autor.title() 
        self.ano = None
        self.editora = None
        self.isbn = None

    def mudar_cor(self, cor: str):
        self.cor = cor.title()
