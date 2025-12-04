from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=4)
data = [['.'] + list(item) + ['.'] for item in puzzle.input_data.split('\n')]
data = [['.'] * len(data[0])] + data + [['.'] * len(data[0])]

answer_a = 0
answer_b = 0

def access(rolls):
    accessible = []
    for row, _ in enumerate(rolls):
        for col, _ in enumerate(rolls[row]):
            if rolls[row][col] == '@':
                adj = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if (i != 0 or j != 0) and rolls[row + i][col + j] == '@':
                            adj += 1
                if adj < 4:
                    accessible += [(row, col)]
    for row, col in accessible:
        rolls[row][col] = '.'
    return rolls, len(accessible)

rolls, removed = access(data)
answer_a += removed
answer_b += removed

while removed > 0:
    rolls, removed = access(rolls)
    answer_b += removed

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b
