from searchPlus import *

class ProblemaGrafoCustos(Problem) :

    grafo = {'I':{'A':2,'B':5},
             'A':{'C':2,'D':4,'I':2},
             'B':{'D':1,'F':5,'I':5},
             'C':{},
             'D':{'C':3,'F':2},
             'F':{}}

    def actions(self,estado) :
        sucessores = self.grafo[estado].keys()
        # obter lista dos sucessores # métodos keys() devolve a lista das chaves do dicionário
        accoes = map(lambda x : "ir de {} para {}".format(estado,x),sucessores) # compor as strings que representam cada uma das possíveis acções
        return list(accoes)
        """
        # alternativamente:
        # accoes = ["ir de {} para {}".format(estado,x) for x in sucessores]
        # return accoes
        #
        # alternaivamente:
        # accoes = list()
        # for x in sucessores :
        #     accoes.append("ir de {} para {}".format(estado,x))
        # return accoes
        """

    def result(self, estado, accao) :
        """Assume-se que uma acção é da forma 'ir de X para Y'
        """
        return accao.split()[-1]

    def path_cost(self, c, state1, action, state2):
        return c + self.grafo[state1][state2]

p = ProblemaGrafoCustos('I','F')

custo = 0
print("Estado inicial:",p.initial, 'com custo',custo)
print("Estado final:",p.goal)
actions = p.actions(p.initial)
e0 = p.initial
print('Cheguei ao objectivo?',p.goal_test(e0))
print("As acções do estado inicial:",str(actions))
e1 = p.result(p.initial,actions[1])
print("Partindo de", p.initial,"executo a acção de " + actions[1]+" e vou parar em :",e1)
custo = p.path_cost(0,p.initial,actions[1],e1)
print("O custo desde o início é:",custo)
print('Cheguei ao objectivo?',p.goal_test(e1))
e2 = p.result(e1,p.actions(e1)[1])
print("Partindo de", e1,"executo a acção de " + p.actions(e1)[1]+" e vou parar em :",e2)
custo = p.path_cost(custo,e1,actions[1],e2)
print("O custo desde o início é:",custo)
print('Cheguei ao objectivo?',p.goal_test(e2))
