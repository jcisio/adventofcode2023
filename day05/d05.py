"""
Advent Of Code
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5
"""
from __future__ import annotations
from collections import defaultdict


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def next_destination(self, v, mapping):
        for m in mapping:
            if m[1] <= v < m[1] + m[2]:
                return m[0] + v - m[1]
        return v

    def last_destination(self, v):
        for m in self.input['maps']:
            v = self.next_destination(v, self.input['maps'][m])
        return v


    def solve(self):
        return min([self.last_destination(seed) for seed in self.input['seeds']])

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        data = {'seeds': list(map(int, input[0].split(': ')[1].split())), 'maps': defaultdict(list)}
        current_map = None
        for line in input[2:]:
            if not line: continue
            if line.endswith(' map:'):
                current_map = line[:-5]
            else:
                data['maps'][current_map].append(list(map(int, line.split())))
        for k in data['maps']:
            data['maps'][k].sort(key=lambda x: x[1])
        self.input = data

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
