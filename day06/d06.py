"""
Advent Of Code
--- Day 6: Wait For It ---
https://adventofcode.com/2023/day/6
"""
from __future__ import annotations
import functools
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def solutions(self, i):
        t = self.input['time'][i]
        d = self.input['distance'][i]
        return sum([1 if j*(t-j)>d else 0 for j in range(t)])

    def solve(self):
        p = 1
        for i in range(len(self.input['time'])):
            p *= self.solutions(i)
        return p

    def solve2(self):
        return self.solve()


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        # Take the time to properly parse the input for part 2. In real life,
        # I searched and replaced all spaces then run part 1 again for part 2.
        t = self.input[0].split(': ')[1]
        d = self.input[1].split(': ')[1]
        problem = Problem({
            'time': list(map(int, (t if part == 1 else t.replace(' ', '')).split())),
            'distance': list(map(int, (d if part == 1 else d.replace(' ', '')).split())),
        })
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
