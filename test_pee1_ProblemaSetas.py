from pee1_ProblemaSetas import *

p = ProblemaSetas()
print(p.initial)

x = EstadoSetas(['d','e','d','e','d','e'])
print(x,"satisfaz o objectivo?",p.goal_test(x))
y = EstadoSetas(['d','d','d','e','d','e'])
print(y,"satisfaz o objectivo?",p.goal_test(y))

p.actions(p.initial)

s1 = p.result(p.initial,1)
print(s1)


s2 = p.result(s1,1)
s2 == p.initial

s3 = p.result(s2,2)
print(s3)
s4 = p.result(s3,3)
print(s4)
s5 = p.result(s4,4)
print(s5)
print("Final?",p.goal_test(s5))
