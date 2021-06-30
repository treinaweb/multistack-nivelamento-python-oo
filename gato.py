from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono


class Gato(Animal, InterfaceAnimal):
    def __init__(self, nome, idade, cor, qtd_bolinhas, dono=Dono()):
        super().__init__(nome, idade, cor)
        self.__qtd_bolinhas = qtd_bolinhas
        self.__dono = dono

    def __str__(self):
        return f"O nome do gato é: {self.nome}. A idade do gato é: {self.idade}" \
               f"A cor do gato é: {self.cor}. A quantidade de bolinhas é: {self.qtd_bolinhas}"

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    @property
    def qtd_bolinhas(self):
        return self.__qtd_bolinhas

    @qtd_bolinhas.setter
    def qtd_bolinhas(self, qtd_bolinhas):
        self.__qtd_bolinhas = qtd_bolinhas

    def fazer_barulho(self):
        return "miau"

    def brincar(self):
        self.felicidade += 1
        return "O gato está brincando"