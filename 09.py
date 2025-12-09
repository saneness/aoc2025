from aocd.models import Puzzle
from shapely.geometry import Polygon

puzzle = Puzzle(year=2025, day=9)
data = [tuple(map(int, item.split(','))) for item in puzzle.input_data.split('\n')]

answer_a = 0
answer_b = 0

polygon = Polygon(data)

for i in range(len(data)):
    for j in range(len(data)):
        if i < j:
            rectangle = Polygon([(data[i][0], data[i][1]), (data[i][0], data[j][1]), (data[j][0], data[j][1]), (data[j][0], data[i][1])])
            area = (max(data[i][0], data[j][0]) - min(data[i][0], data[j][0]) + 1) * (max(data[i][1], data[j][1]) - min(data[i][1], data[j][1]) + 1)
            answer_a = max(answer_a, area)
            if polygon.contains(rectangle):
                answer_b = max(answer_b, area)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b