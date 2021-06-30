import abc


class InterfaceAnimal(abc.ABC):
    @abc.abstractmethod
    def fazer_barulho(self):
        pass

    @abc.abstractmethod
    def brincar(self):
        pass