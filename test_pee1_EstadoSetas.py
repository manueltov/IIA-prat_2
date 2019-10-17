from pee1_EstadoSetas import *

"""TEST ESTADO SETAS"""
x = EstadoSetas(["d","e","d","d","d","e"])
print("Começamos com:",x)
y = x.inverte(1)
print("Agora, inverte a primeira e a segunda:",y)
z = y.inverte(2)
print("E inverte a segunda e terceira setas:",z)
f = z.inverte(2).inverte(1)
print("Façamos o inverso das duas inversões:",f)
print("Os dois estados (o original e este que resulta de 4 acções) serão iguais?",f==x)

EstadoSetas(["d","e","d","d","d","e"]) == EstadoSetas(["d","e","d","d","d","e"])
