from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=5)
data = puzzle.input_data.split('\n\n')
data[0] = [tuple((int(subitem) for subitem in item.split('-'))) for item in data[0].split('\n')]
data[1] = [int(item) for item in data[1].split('\n')]

answer_a = 0
answer_b = 0

for ingridient in data[1]:
    fresh = False
    for low, high in data[0]:
        if low <= ingridient <= high:
            fresh = True
    if fresh:
        answer_a += 1

def collapse(ranges):
    ranges_collapsed = []
    prev_range = ranges[0]
    for low, high in ranges[1:]:
        if prev_range[1] < low:
            ranges_collapsed += [prev_range]
            prev_range = (low, high)
        else:
            prev_range = (prev_range[0], max(prev_range[1], high))
    if prev_range not in ranges_collapsed:
        ranges_collapsed += [prev_range]
    return ranges_collapsed

answer_b = sum([range[1] - range[0] + 1 for range in collapse(sorted(data[0], key=lambda x: x[0]))])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b