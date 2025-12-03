from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=3)
data = puzzle.input_data.split('\n')

answer_a = 0
answer_b = 0

for bank in data:
    answer_a += int(max(bank[:-1]) + max(bank[bank.index(max(bank[:-1]))+1:]))

    number = 0
    i = 12
    while(len(bank)) > i > 0:
        next = max(bank[:-i+1]) if i != 1 else max(bank)
        bank = bank[bank.index(next)+1:]
        number = int(str(number) + next)
        i -= 1

    if i > 0:
        number = int(str(number) + bank)
    
    answer_b += number

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b