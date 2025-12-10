from aocd.models import Puzzle
import itertools
import functools
import numpy
from scipy.optimize import LinearConstraint
from scipy.optimize import milp

puzzle = Puzzle(year=2025, day=10)
data = [[subitem[1:-1] for subitem in item.split()] for item in puzzle.input_data.split('\n')]

answer_a = 0
answer_b = 0

for item in data:
    target = int(item[0].replace('.', '0').replace('#', '1')[::-1], 2)
    wirings = [set(map(int, subitem.split(','))) for subitem in item[1:-1]]
    joltage = list(map(int, item[-1].split(',')))
    
    lowest = 0

    for i in range(1, len(wirings)):
        for combination in itertools.combinations(wirings, i):
            current = sum([2**number for number in functools.reduce(lambda x, y: x ^ y, combination)])
            if current == target:
                lowest = i
                break
        if lowest > 0:
            break
    
    answer_a += lowest

    c = numpy.array([1] * len(wirings))
    
    f = []
    for i in range(len(joltage)):
        f.append([1 if i in wiring else 0 for wiring in wirings])
    a = numpy.array(f)

    b_u = numpy.array(joltage)
    b_l = b_u

    constraints = LinearConstraint(a, b_l, b_u)
    integrality = numpy.ones_like(c)

    res = milp(c=c, constraints=constraints, integrality=integrality).fun

    answer_b += round(res)

print(answer_a)
print(answer_b)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b