from abc import ABC, abstractmethod
class Anestesico(ABC):
    
    def __init__(self, concentracao:'mg/mL'):
        self.__concentracao = concentracao

    @abstractmethod
    def calcula(self, roedor: 'Roedor') -> 'mL':
        pass

class Tiopental(Anestesico):
    
    def __init__(self, concentracao:'mg/mL'=25):
        self.__concentracao = concentracao

    def calcula(self, roedor: 'Roedor') -> 'mL':
        return ((roedor.peso/1000)*40)/self.__concentracao

class Propofol(Anestesico):
    def __init__(self, concentracao:'mg/mL'=10):
        self.__concentracao = concentracao

    def calcula(self, roedor: 'Roedor') -> 'mL':
        return ((roedor.peso/1000)*10)/self.__concentracao

class Roedor():
    def __init__(self, id: str, peso: 'g'):
        self.__id = id
        self.__peso = peso
    
    @property
    def peso(self) -> 'g':
        return self.__peso


class DosagemAnestesica():
    
    def __init__(self):
        pass

    def calcula_dosagem(self, roedor: 'Roeador', anestesico) -> 'mL':
        return anestesico.calcula(roedor)

if __name__ == '__main__':

    rato = Roedor(id="V1", peso=300)
    dose = DosagemAnestesica()
    print(f'Dose de Tiopental: {dose.calcula_dosagem(rato, Tiopental())} mL')
    print(f'Dose de Propofol: {dose.calcula_dosagem(rato, Propofol())} mL')