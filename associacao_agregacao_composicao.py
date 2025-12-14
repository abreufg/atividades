#1
class Motor:
    def ligar(self):
        print("Motor ligado.")


class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()  # composição

    def ligar_carro(self):
        print(f"Carro {self.modelo} ligado.")
        self.motor.ligar()


carro = Carro("Fusca")
carro.ligar_carro()


#2

class Professor:
    def __init__(self, nome):
        self.nome = nome


class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []  # agregação

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        for p in self.professores:
            print(p.nome)


prof1 = Professor("Carlos")
prof2 = Professor("Ana")

uni = Universidade("UFMA")
uni.adicionar_professor(prof1)
uni.adicionar_professor(prof2)

uni.listar_professores()


#3
class Autor:
    def __init__(self, nome):
        self.nome = nome


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor  # associação

    def detalhes(self):
        print(f"Livro: {self.titulo} | Autor: {self.autor.nome}")


autor = Autor("Machado de Assis")
livro = Livro("Dom Casmurro", autor)

livro.detalhes()




