from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=7)
data = [list(item) for item in puzzle.input_data.split('\n')]

answer_a = 0
answer_b = 0

start = data[0].index('S')
data[1][start] = 1

for i in range(2, len(data)):
    if i % 2 == 0:
        for j in range(len(data[i])):
            if isinstance(data[i-1][j], int):
                if data[i][j] == '^':
                    for k in [-1, 1]:
                        if isinstance(data[i][j+k], int):
                            data[i][j+k] += data[i-1][j]
                        else:
                            data[i][j+k] = data[i-1][j]
                        data[i+1][j+k] = data[i][j+k]
                    answer_a += 1
                else:
                    if isinstance(data[i][j], int):
                        data[i][j] += data[i-1][j]
                    else:
                        data[i][j] = data[i-1][j]
                    data[i+1][j] = data[i][j]

answer_b = sum([item for item in data[-1] if isinstance(item, int)])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b