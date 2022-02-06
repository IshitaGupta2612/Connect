#Towards Data Code->Last piece
from pulp import *
prob = LpProblem("Matching Employees", LpMaximize)

import numpy as np 
import pandas as pd
employees = range(8)
names =['Ben','Kate','Thinh','Jorge','Alfredo','Francisco','Olivia','Chris']
c = np.array([
        [0, 0, -3, -3, -7, -9, -3, -5],
        [2, 0, 7, 6, 8, 8, 1, 6],
        [7, 7, 0, 1, 5, 9, 8, 9],
        [4, 3, 0, 0, 5, 0, 2, 3],
        [8, 1, 3, 3, 0, 7, 0, 1],
        [9, 9, 0, 4, 7, 0, 2, 7],
        [2, 0, 0, 4, 5, 5, 0, 8],
        [4, 1, 4, 9, 8, 1, 1, 0]
    ])

y = LpVariable.dicts("pair", [(i,j) for i in employees for j in employees] ,cat='Binary')

prob += lpSum([(c[i][j] + c[j][i]) * y[(i,j)] for i in employees for j in employees])

for i in employees:
    prob += lpSum(y[(i,j)] for j in employees) <= 1
    prob += lpSum(y[(j,i)] for j in employees) <= 1
    prob += lpSum(y[(i,j)] + y[(j,i)] for j in employees) <= 1
prob += lpSum(y[(i,j)] for i in employees for j in employees) == 4

prob.solve()

print("Finish matching!\n")
for i in employees:
    for j in employees:
        if y[(i,j)].varValue == 1:
            print('{} and {} with preference score {} and {}. Total score: {}'.format(names[i],names[j],c[i,j], c[j,i], c[i,j] +c[j,i]))