from searchPlus import *

class ProblemaGrafo(Problem) :

    def __init__(self, initial, goal=None) :
        self.initial = initial
        self.goal = goal

    def actions(self,estado) :
        sucessores = self.grafo[estado]  # obter lista dos sucessores
        accoes = map(lambda x : "ir de {} para {}".format(estado,x),sucessores) # compor as strings que representam cada uma das possíveis acções
        return list(accoes)

    def result(self, estado, accao) :
        """Assume-se que uma acção é da forma 'ir de X para Y'
        """
        return accao.split()[-1]


p1 = ProblemaGrafo('I','F')

p1.grafo = {'I':['A','B'],
         'A':['C','D','I'],
         'B':['D','F','I'],
         'C':[],
         'D':['C','F'],
         'F':[]}

print("Estados:")
for estado in p1.grafo.keys():
    print(estado)
print("\n")

custo=0
e0 = p1.initial
print('Em',e0,'com custo',custo)
print('Cheguei ao objectivo?',p1.goal_test(e0))
a1 = p1.actions(e0)[0]
e1 = p1.result(e0,a1)
custo = p1.path_cost(custo,e0,a1,e1)
print('Após executar a 1ª acção:', a1, 'passei para ',e1, ', com custo',custo)
print('Cheguei ao objectivo?',p1.goal_test(e1))
a2 = p1.actions(e1)[0]
e2 = p1.result(e1,a2)
custo = p1.path_cost(custo,e1,a2,e2)
print('Após executar a 2ª acção:', a2, 'passei para ',e2, ', com custo',custo)
print('Cheguei ao objectivo?',p1.goal_test(e2))
