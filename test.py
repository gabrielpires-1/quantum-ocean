'''
Esse código utiliza o solucionador ExactSolver() para resolver o QUBO. O método ExactSolver() utiliza um simulador clássico na própria máquina para solucionar o problema do QUBO, e não em um computador da D WAVE.
'''

import dimod

## get the solver
solver = dimod.ExactSolver()

## define the QUBO - Quadratic Uncostrained Binary Optimization
Q = {('a','b'):-2,('a','a'):1,('b','b'):1}

## get the bqm
bqm = dimod.BinaryQuadraticModel.from_qubo(Q)

## solve the problem 
results = solver.sample(bqm)

## print the result
print(results)

'''
   a  b energy num_oc.
0  0  0    0.0       1
2  1  1    0.0       1
1  1  0    1.0       1
3  0  1    1.0       1
'''