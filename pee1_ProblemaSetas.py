from searchPlus import *
from pee1_EstadoSetas import *

class ProblemaSetas(Problem) :

    def __init__(self,initial = EstadoSetas(["e","e","e","d","d","d"]),goal=[EstadoSetas(["e","d","e","d","e","d"]),EstadoSetas(["d","e","d","e","d","e"])]) :
        super().__init__(initial,goal)


    def actions(self,estado) :
        """ A acção 0 corresponde a inverter as setas de índices 0 e 1 da lista
            A acção 4 coorresponde a inverter as setas de índices 4 e 5, as últimas duas """
        accoes = [1,2,3,4,5]

        return accoes

    def result(self,estado,acao) :
        if acao in self.actions(estado) :
          resultante = estado.inverte(acao)
        else :
            raise "Há aqui qualquer coisa mal>> acao não reconhecida"

        return resultante
