from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2025, day=12)
data = [map(int, re.split("\D+", item)) for item in puzzle.input_data.split("\n\n")[-1].split("\n")]

answer_a = sum([w * h >= sum(nums) * 9 for w, h, *nums in data])

puzzle.answer_a = answer_a