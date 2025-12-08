from aocd.models import Puzzle
import math
import itertools

puzzle = Puzzle(year=2025, day=8)
data = puzzle.input_data.split('\n')

answer_a = 0
answer_b = 0

def merge(links):
    to_merge = False
    for i, source in enumerate(links):
        for j, target in enumerate(links):
            if i < j and source & target:
                to_merge = True
                break
        if to_merge:
            break
    if to_merge:
        return [link for link in links if links.index(link) not in (i, j)] + [links[i] | links[j]]
    else:
        return links
    
def prod(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

distances = {}

for i, source in enumerate(data):
    for j, target in enumerate(data):
        if i < j:
            x1, y1, z1 = [int(item) for item in source.split(',')]
            x2, y2, z2 = [int(item) for item in target.split(',')]
            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            distances.update({source + ':' + target: distance})

distances = list(item.split(':') for item in {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}.keys())

links = []
links_number = 0
links_number_max = 1000

for pair in distances:
    linked = False
    for i, link in enumerate(links):
        if pair[0] in link or pair[1] in link:
            links[i].add(pair[0])
            links[i].add(pair[1])
            linked = True
            links_number += 1
        if linked:
            break
    if not linked:
        links += [set(pair)]
        links_number += 1
    links = merge(links)
    if links_number == links_number_max:
        answer_a = prod(sorted([len(item) for item in links])[-3:])
    if len(links) == 1:
        linked = True
        for item in data:
            if item not in links[0]:
                linked = False
                break
        if linked:
            answer_b = prod([int(item.split(',')[0]) for item in pair])
            break

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b