from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono


class Cachorro(Animal, InterfaceAnimal):
    def __init__(self, nome, idade, cor, qtd_brinquedos, dono=Dono()):
        super().__init__(nome, idade, cor)
        self.__qtd_brinquedos = qtd_brinquedos
        self.__dono = dono

    def __str__(self):
        return f"O nome do cachorro é: {self.nome}. A idade do cachorro é: {self.idade}" \
               f"A cor do cachorro é: {self.cor}. A quantidade de brinquedos é: {self.qtd_brinquedos}"

    @property
    def qtd_brinquedos(self):
        return self.__qtd_brinquedos

    @qtd_brinquedos.setter
    def qtd_brinquedos(self, qtd_brinquedos):
        self.__qtd_brinquedos = qtd_brinquedos

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    def fazer_barulho(self):
        return "au au"

    def brincar(self):
        self.felicidade += 2
        return "O cachorro está brincando"