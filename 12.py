from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=12)
data = puzzle.input_data.split('\n\n')

shapes = data[:-1]
regions = data[-1].split('\n')
sizes = [sum(c == "#" for c in shape) for shape in shapes]

answer_a = 0

for region in regions:
    w, h = map(int, region.split(":")[0].split("x"))
    nums = map(int, region.split(":")[1].split())
    if w * h >= sum(n * size for n, size in zip(nums, sizes)):
        answer_a += 1

puzzle.answer_a = answer_a