from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=11)
data = {item.split(":")[0]: item.split(":")[1].split() for item in puzzle.input_data.split('\n')}

answer_a = 0
answer_b = 0

def path_count(paths, start, end, cache):
    if start in cache:
        return cache[start]
    elif start not in paths:
        cache[start] = 0
        return 0
    else:
        result = sum([path_count(paths, path, end, cache) for path in paths[start]])
        cache[start] = result
        return result

answer_a = path_count(data, "you", "out", {"out": 1})
answer_b = path_count(data, "svr", "fft", {"fft": 1}) * path_count(data, "fft", "dac", {"dac": 1}) * path_count(data, "dac", "out", {"out": 1}) + path_count(data, "svr", "dac", {"dac": 1}) * path_count(data, "dac", "fft", {"fft": 1}) * path_count(data, "fft", "out", {"out": 1})

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b