"""
Advent Of Code
--- Day 15: Lens Library ---
https://adventofcode.com/2023/day/15
"""
from __future__ import annotations
from collections import defaultdict
import re


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def hash(self, s):
        h = 0
        for c in s:
            h = (h + ord(c)) * 17 % 256
        return h

    def solve(self):
        return sum(self.hash(m) for m in self.input)

    def solve2(self):
        boxes = [[] for _ in range(256)]
        for m in self.input:
            label, op, focal = re.match(r'(\w+)([\-\=])(\d*)', m).groups()
            h = self.hash(label)
            if op == '-':
                boxes[h] = [lens for lens in boxes[h] if lens[0] != label]
            elif op == '=':
                found = False
                for lens in boxes[h]:
                    if lens[0] == label:
                        lens[1] = focal
                        found = True
                        break
                if not found:
                    boxes[h].append([label, focal])
            s = 0
            for i, box in enumerate(boxes):
                for j, lens in enumerate(box):
                    s += (i+1) * (j+1) * int(lens[1])
        return s


class Solver:
    def __init__(self, input) -> None:
        self.input = input.split(',')

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip())
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
