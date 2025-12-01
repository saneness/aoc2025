from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=1)
data = [int(item.replace("L", "-").replace("R", "")) for item in puzzle.input_data.split('\n')]

pos = 50
answer_a = 0
answer_b = 0

for item in data:
    prev_pos = pos
    sign = 1 if item > 0 else -1
    pos += sign * (abs(item) % 100)
    
    while pos >= 100:
        pos -= 100
        answer_b += 1 if pos != 0 and prev_pos != 0 else 0
    while pos < 0:
        pos += 100
        answer_b += 1 if pos != 0 and prev_pos != 0 else 0
    
    if pos == 0:
        answer_a += 1
        answer_b += 1

    answer_b += abs(item) // 100

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b