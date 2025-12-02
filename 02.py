from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=2)
data = [tuple(int(subitem) for subitem in item.split('-')) for item in puzzle.input_data.split(',')]

def invalid_a(number):
    number_len = len(str(number))
    if number_len % 2 == 0:
        if number % (10 ** (number_len // 2) + 1) == 0:
            return True
    return False
    
def invalid_b(number):
    number_len = len(str(number))
    for i in range(1, number_len // 2 + 1):
        if number_len % i == 0:
            mask = int(str(("1" + "0" * (i - 1)) * (number_len // i))[::-1])
            if number % mask == 0:
                return True
    return False

answer_a = 0
answer_b = 0

for low, high in data:
    for number in range(low, high + 1):
        if invalid_a(number):
            answer_a += number
        if invalid_b(number):
            answer_b += number

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b