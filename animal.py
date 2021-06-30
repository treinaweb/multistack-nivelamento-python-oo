import abc

class Animal(abc.ABC):
    def __init__(self, nome, idade, cor, felicidade=0):
        self._nome = nome
        self._idade = idade
        self._cor = cor
        self._felicidade = felicidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def felicidade(self):
        return self._felicidade

    @felicidade.setter
    def felicidade(self, felicidade):
        self._felicidade = felicidade
