from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=6)
data = [item + ' ' for item in puzzle.input_data.split('\n')]

numbers = [item.split() for item in data[:-1]]
operators = data[-1].split()

answer_a = 0
answer_b = 0

def prod(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

for i in range(len(operators)):
    current = [int(row[i]) for row in numbers]
    if operators[i] == '+':
        answer_a += sum(current)
    if operators[i] == '*':
        answer_a += prod(current)

for i in range(len(data[0])):
    if data[-1][i] != ' ':
        operator = data[-1][i]
        current = []
    number = ''.join([row[i] for row in data[:-1]]).strip()
    if len(number) > 0:
        current += [int(number)]
    else:
        if operator == '+':
            answer_b += sum(current)
        if operator == '*':
            answer_b += prod(current)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b