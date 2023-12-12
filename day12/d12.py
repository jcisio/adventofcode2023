"""
Advent Of Code
--- Day 12: Hot Springs ---
https://adventofcode.com/2023/day/12
"""
from __future__ import annotations
from collections import defaultdict
import itertools
import re
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def is_ok(self, parts, groups):
        #print(parts, groups)
        return list(map(len, re.sub(r'\.+', '.', parts.strip('.')).split('.'))) == groups

    def solve(self):
        s = 0
        for parts, groups in self.input:
            damaged = sum(groups) - parts.count('#')
            possible_places = [m.start() for m in re.finditer(r'\?', parts)]
            if damaged > len(possible_places):
                raise Exception(f'Wrong input {parts} {groups}')
            parts = list(parts)
            for p in itertools.combinations(possible_places, damaged):
                for j in possible_places:
                    if j in p:
                        parts[j] = '#'
                    else:
                        parts[j] = '.'
                if self.is_ok(''.join(parts), groups):
                    #print(parts)
                    s += 1
        return s

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        rows = []
        for row in input:
            parts, groups = row.split()
            rows.append((parts, list(map(int, groups.split(',')))))
        self.input = rows

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
